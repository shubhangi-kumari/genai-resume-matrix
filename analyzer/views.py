import os
import google.generativeai as genai
from django.shortcuts import render, redirect
from django.http import JsonResponse
from PyPDF2 import PdfReader
from .forms import ResumeForm

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text() + '\n'
    return text

def home(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()
            text = extract_text_from_pdf(resume.resume_file.path)
            
            # Gemini Prompts
            prompts = {
                'highlights': f"Extract key skills, projects, and keywords from this resume text. Format as JSON: {{'skills': [...], 'projects': [...], 'keywords': [...]}}. Resume: {text}",
                'rating': f"Rate this resume for clarity and impact out of 10. Respond with just the number.",
                'suggestions': f"Provide 3-5 bullet-point suggestions for improvement in sections (e.g., skills, projects). Keep professional and concise. Resume: {text}",
                'summary': f"Generate a concise 2-line professional summary that captures attention. Resume: {text}",
                'comparison': lambda job: f"Compare this resume to a '{job}' role. List 3-5 missing skills. Resume: {text}" if job else None
            }
            
            results = {}
            for key, prompt in prompts.items():
                if key == 'comparison' and not form.cleaned_data['job_title']:
                    continue
                if callable(prompt):
                    response = model.generate_content(prompt(form.cleaned_data['job_title']))
                else:
                    response = model.generate_content(prompt)
                results[key] = response.text.strip()
            
            # Parse highlights JSON
            import json
            try:
                results['highlights'] = json.loads(results['highlights'])
            except:
                results['highlights'] = {'skills': [], 'projects': [], 'keywords': []}
            
            # Store results and job title in session
            request.session['results'] = results
            request.session['job_title'] = form.cleaned_data['job_title']  # Store job title
            
            return redirect('analyze')  # Redirect to analyze view
    else:
        form = ResumeForm()
    return render(request, 'home.html', {'form': form})

def analyze_resume(request):
    # Fetch results from session
    results = request.session.get('results', {})
    job_title = request.session.get('job_title', '')
    
    # Render the analyze.html template with results and job title
    return render(request, 'analyze.html', {
        'results': results,
        'job_title': job_title
    })

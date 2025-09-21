# 🚀 MatrixResumeForge: Hack The Matrix with GenAI Resumes!  

![Matrix Banner](https://via.placeholder.com/1200x400/000000/00FF00?text=Hack+The+Matrix+-+Resume+Forge)  
<!-- Banner image: Create in Canva, Matrix-style -->

## 🎯 Problem Solved
Are resumes failing to impress recruiters?  
MatrixResumeForge lets you:
- Upload your PDF resume
- Extract skills and highlights using **Gemini AI**
- Get a **clarity & impact rating**
- Receive **section-wise suggestions**
- Generate an **attention-grabbing 2-line summary**

Optional: Compare your resume against a target job title to identify missing skills.  

**Theme Tie-In:** Like Neo in the Matrix, dodge resume gaps with AI holograms!  

## ✨ Key Features
- **Extract Highlights:** Skills, projects, keywords (JSON parsed via Gemini)  
- **Quick Rating:** Score clarity & impact out of 10  
- **Smart Suggestions:** Section-wise improvements for maximum effect  
- **Pro Summary:** Create a 2-liner that grabs attention  
- **Job Comparison:** Identify missing skills for your target role  
- **Unique Twist:** 3D Skill Tree (**Three.js**) + Matrix Rain Background — spinning holograms showcase your strengths  

![Home Screenshot](screenshots/home-upload.png)  
![Analysis Screenshot](screenshots/analyze-3d-tree.gif)  

## 🛠 Tech Stack
- **Backend:** Django 4.2, PyPDF2 for PDF extraction  
- **AI:** Google Gemini API (free tier — prompts for JSON & rating)  
- **Frontend:** HTML/JS with Three.js for immersive 3D visuals  
- **Deployment:** [Live Demo Link] (if deployed)  

## 📹 Demo Video
Watch the magic: [YouTube Link - 1:45 min demo]  
*(Demo for GenAI-Powered Solutions: Hack The Matrix")*  

## 🚀 Quick Start
```bash
# Clone the repo
git clone https://github.com/shubhangi-kumari/genai-resume-matrix.git

# Install dependencies
pip install -r requirements.txt

# Set API key
export GEMINI_API_KEY="your_api_key_here"  # Linux/Mac
set GEMINI_API_KEY="your_api_key_here"     # Windows

# Run the server
python manage.py runserver

from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
from flask import Flask

def optimise_cv(job_desc, file_bytes):
    load_dotenv()
    API_KEY = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=API_KEY)
    prompt = '''
    Role: You are a senior HR consultant and ATS (Applicant Tracking System) optimisation expert with 8 years of experience at top tech companies like Google, Microsoft, and startups. You've reviewed over 10,000 CVs and know exactly what hiring managers look for. Your specialty is helping candidates get past ATS filters and land interviews by optimising keyword usage, formatting, and content structure.
    Context: 75% of CVs are filtered out by ATS systems. Analyse this CV against the job requirements and optimise for keyword matching and relevance. Make sure the uploaded CV shows skills they talk about instead of just telling using action verbs and quantifying achievements. 
    Examples: 
    BAD: "Responsible for managing projects"
    GOOD: "Led agile teams of 8+ developers, delivered 15 projects on time with 23% budget savings"
    BAD: "Improved system performance"  
    GOOD: "Optimised database queries, reduced load times by 67%"
    Analysis format:
    MATCH SCORE: [X/100]
    MISSING KEYWORDS: [3-5 key terms from job description]
    STRENGTHS: [2-3 existing strong points]
    IMPROVEMENTS: [3 specific changes to make]
    OPTIMISED SUMMARY: [2-3 sentences incorporating missing keywords]
    '''
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=[
        types.Part.from_bytes(
            data=file_bytes,
            mime_type='application/pdf',
        ),
        prompt, job_desc],
    )
    return(response.text)
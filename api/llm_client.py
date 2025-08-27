import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# set up the client with the key
genai.configure(api_key=API_KEY)

def optimise_cv(job_desc, file_path):

    # this is the prompt that tells the ai what to do
    prompt = '''
    Role: You are a senior HR consultant and ATS (Applicant Tracking System) optimisation expert with 8 years of experience at top tech companies like Google, Microsoft, and startups. You've reviewed over 10,000 CVs and know exactly what hiring managers look for. Your specialty is helping candidates get past ATS filters and land interviews by optimising keyword usage, formatting, and content structure. Make sure the uploaded CV shows skills they talk about instead of just telling using action verbs and quantifying achievements. Compare the CV that has been uploaded against a perfect CV for the job description that they are looking at. Use British english. Some of the key changes I want you to make include: shorter sentences, bullet points for scannability, stronger action words, and leading with the problem/solution rather than explaining the job market situation.
    Context: 75% of CVs are filtered out by ATS systems. Analyse this CV against the job requirements and optimise for keyword matching and relevance.
    Examples: 
    BAD: "Responsible for managing projects"
    GOOD: "Led agile teams of 8+ developers, delivered 15 projects on time with 23% budget savings"
    BAD: "Improved system performance"  
    GOOD: "Optimised database queries, reduced load times by 67%"
    Analysis format:
    - The CV they uploaded with the optimisations to all of the sections, like the optimisations shown in the exmaple, ensuring the format of the CV is kept the same as the one they have uploaded. 
    Relevance score: x/100
    Missing keywords: Ranked list of keywords missing from the CV that the job description repeats (3-5 of them)
    Strengths: 2-3 existing strong points
    Improvements: 3 specific changes to make
    '''

    uploaded_file = genai.upload_file(path=file_path)

    # send the file and prompt the ai and get a response
    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(
        contents=[
            uploaded_file,
            prompt,
            job_desc
        ],
    )

    # return the text from the response
    return(response.text) 
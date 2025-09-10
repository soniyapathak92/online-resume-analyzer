import fitz #pymupdf
import google.generativeai as genai
from analyse import analyse_resume_gemini


#function to text from the resume
def  extract_text_from_resume(pdf_path):
    doc = fitz.open(pdf_path)
    text= ""
    for page in doc:
        text+=page.get_text()
    return text

pdf_path=pdf_path = "soniya pathak resume.pdf"
print(extract_text_from_resume(pdf_path))

job_description= """
We are looking for a Python Developerwith experience 
in web frameworks, REST APIs, and cloud platforms.
Key skills required: Python, Django/Flask, REST API, SQL, Git.
Responsibilities include developing backend services, collaborating with frontend developers, and optimizing applications for performance.
"""
result=analyse_resume_gemini(extract_text_from_resume(pdf_path),job_description)
print("Resume Analysis:\n")
print(result)
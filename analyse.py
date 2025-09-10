import google.generativeai as genai
from dotenv import load_dotenv
import  os

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

configuration={
    "temperature":1,
    "top_p":0.95,
    "top_k":40,
    "max_output_tokens":8192,
    "response_mime_type":"text/plain"
    }
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash",
    generation_config=configuration
)

def analyse_resume_gemini(resume_content,job_description):
    prompt=(
        "You are an expert resume analyzer. "
        "Given the following resume and job description, provide a detailed analysis including:\n"
        "- Key skills match\n"
        "add a portofolio link"
        "- Areas for improvement\n"
        "-suggest improvments\n"
        "Resume:\n"
        "return the result in structured format:"
        "match score:xx/100"
        "missing skills:"
        f"{resume_content}\n\n"
        "Job Description:\n"
        f"{job_description}\n"
    )
    response=model.generate_content(prompt)
    return response.text
    
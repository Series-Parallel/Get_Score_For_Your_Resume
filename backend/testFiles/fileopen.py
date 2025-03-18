import fitz  # type: ignore
from utils.preprocess import extract_text_from_pdf, extract_resume_info

# Open the file in binary mode
with open("Deo_Pathak.pdf", "rb") as pdf_file:
    resume_text = extract_text_from_pdf(pdf_file)

print("1", resume_text)

resume_info = extract_resume_info(resume_text)
print("2", resume_info)

candidate_skills = resume_info["skills"]
print("3", candidate_skills)

candidate_location = resume_info["location"]
print("4", candidate_location)

candidate_experience = resume_info["experience"]
print("5", candidate_experience)

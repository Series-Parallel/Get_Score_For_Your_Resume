import pickle
import re
import fitz  # type: ignore # PyMuPDF for extracting text from PDFs

from sklearn.metrics.pairwise import cosine_similarity # type: ignore
import spacy  # type: ignore
from datetime import datetime

def extract_job_info(job_desc):
    required_skills = re.search(r"Required Skills:\s*(.*?)(?=\n|Preferred Skills:|$)", job_desc, re.IGNORECASE | re.DOTALL)
    preferred_skills = re.search(r"Preferred Skills:\s*(.*?)(?=\n|$)", job_desc, re.IGNORECASE | re.DOTALL)
    location = re.search(r"Location:\s*([^\n,]+)", job_desc, re.IGNORECASE)
    experience = re.search(r"Experience:\s*([\d\-+ years]+)", job_desc, re.IGNORECASE)

    required_skills = required_skills.group(1).strip() if required_skills else ""
    preferred_skills = preferred_skills.group(1).strip() if preferred_skills else ""

    combined_skills = required_skills + (", " + preferred_skills if preferred_skills else "")

    return {
        "job_skills": combined_skills,
        "location": location.group(1).strip() if location else "",
        "experience": experience.group(1).strip() if experience else "",
    }


def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = " ".join([page.get_text("text") for page in doc])
    return text.lower()

nlp = spacy.load("en_core_web_sm")

def extract_experience_from_resume(resume_text):
    """Extracts experience in years from resume based on start and end dates."""
    date_patterns = [
        r"(\w{3,9} \d{4})\s*[-–]\s*(\w{3,9} \d{4})",  # Supports full and short month names
        r"(\w{3,9} \d{4})\s*[-–]\s*(Present|present)",  # Format: May 2024 – Present
    ]

    total_experience_months = 0
    current_year = datetime.now().year
    current_month = datetime.now().month

    for pattern in date_patterns:
        matches = re.findall(pattern, resume_text)
        for start, end in matches:
            try:
                start_date = datetime.strptime(start, "%B %Y")
                if "present" in end.lower():
                    end_date = datetime(current_year, current_month, 1)
                else:
                    end_date = datetime.strptime(end, "%B %Y")

                months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                total_experience_months += max(0, months)  # Ensure no negative values
            except ValueError:
                continue

    total_experience_years = round(total_experience_months / 12, 1)  # Convert to years, rounded
    return total_experience_years

def extract_skills(resume_text):
    """Extracts skills from any section containing 'Skills'."""
    skills_match = re.search(r"(.*?Skills.*?)\n([\s\S]+?)(\n[A-Z][a-z]+:|\Z)", resume_text, re.IGNORECASE)

    if skills_match:
        skills_section = skills_match.group(2).strip()  # Extract skills content
        skills_lines = skills_section.split("\n")
        
        # Remove unwanted characters and join into a single line
        skills_text = " ".join(line.strip() for line in skills_lines if len(line.strip()) > 2)
    else:
        skills_text = ""

    return skills_text

def extract_resume_info(resume_text):
    """Extracts skills, location, and experience from resume text."""
    skills_text = extract_skills(resume_text)  # Updated skill extraction method

    doc = nlp(resume_text)
    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE" and len(ent.text) > 2]  # Better location filtering

    experience_years = extract_experience_from_resume(resume_text)

    return {
        "skills": skills_text,
        "experience": experience_years,
        "location": locations[0] if locations else "",
    }

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def compute_tfidf_similarity(text1, text2):
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    return similarity_score

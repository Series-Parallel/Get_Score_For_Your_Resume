from flask import Flask, request, jsonify
import pickle
import numpy as np
from utils.preprocess import extract_text_from_pdf, extract_job_info, extract_resume_info, compute_tfidf_similarity
from flask_cors import CORS #type: ignore
import pandas as pd

app = Flask(__name__)
CORS(app)

with open("job_match_model.pkl", "rb") as f:
    model = pickle.load(f)

feature_names = ['skill_match_score' ,'is_same_country', 'experience_match']


@app.route("/api/compare-resume", methods=["POST"])
def compare_resume():
    print("🚀 API route hit!", flush=True)
    try:
        # Get job description from request
        job_desc = request.form.get("jobDescription")
        resume_file = request.files["resume"]

        if not job_desc or not resume_file:
            return jsonify({"error": "Job description and resume file are required"}), 400

        # Extract job details
        job_info = extract_job_info(job_desc)
        job_skills = job_info["job_skills"]
        job_location = job_info["location"]
        job_experience_range = job_info["experience"]  # Experience range (e.g., "2-4 years")

        # Extract resume details
        resume_text = extract_text_from_pdf(resume_file)
        resume_info = extract_resume_info(resume_text)
        candidate_skills = resume_info["skills"]
        candidate_location = resume_info["location"]
        candidate_experience = resume_info["experience"]

        # Compute skill match score
        skill_match_score = compute_tfidf_similarity(job_skills, candidate_skills)

        # Compute country match (1 if same, else 0)
        is_same_country = int(candidate_location.lower() in job_location.lower())

        # Compute experience match (0 if less, 1 if in range, 2 if greater)
        exp_min, exp_max = 0, 0
        if job_experience_range:
            exp_values = [int(num) for num in job_experience_range.split() if num.isdigit()]
            if len(exp_values) == 2:
                exp_min, exp_max = exp_values
            elif len(exp_values) == 1:
                exp_min = exp_values[0]

        if candidate_experience < exp_min:
            experience_match = 0
        elif exp_min <= candidate_experience <= exp_max:
            experience_match = 1
        else:
            experience_match = 2

        # Prepare input for model
        input_features = pd.DataFrame([[skill_match_score ,is_same_country, experience_match]], 
                              columns=feature_names)
        print("Input Features:\n", input_features, flush=True)

       
        final_score = model.predict(input_features)[0]


        return jsonify({
            "is_same_country": is_same_country,
            "experience_match": experience_match,
            "skill_match_score": round(skill_match_score, 3),
            "final_score": round(final_score, 2)
        })

    except Exception as e:
        print("🔥 Error during prediction:", str(e), flush=True)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)

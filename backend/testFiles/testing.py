import joblib
import pandas as pd

feature_names = ['skill_match_score' ,'is_same_country', 'experience_match']
model = joblib.load("job_match_model.pkl")

skill_match_score = 0.8
is_same_country = 1
experience_match = 1

input_features = pd.DataFrame([[skill_match_score ,is_same_country, experience_match]], 
                              columns=feature_names)
final_score = model.predict(input_features)[0]

print("Final Score:", final_score)
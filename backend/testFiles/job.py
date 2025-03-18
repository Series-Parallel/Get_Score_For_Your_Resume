from utils.preprocess import extract_job_info

job_desc = "Location: USA, Experience: 0-5 years We're seeking talented interns to join our team in developing an innovative AI-powered platform with voice and video capabilities. Responsibilities: Develop AI components for chat and speech summarization Implement video and audio recording features Assist in creating algorithms to convert video/voice content into text summaries Contribute to the integration of LLMs for various platform functionalities Help with testing and improving the user experience Collaborate with the team on various aspects of the SaaS platform Required Skills: Strong programming skills (Python preferred) Experience with machine learning and LLMs (Large Language Models) Familiarity with natural language processing (NLP) and text summarization technique Basic understanding of speech recognition and audio processing Experience with video and audio handling libraries Preferred Skills: Knowledge of cloud platforms (AWS, Azure, or GCP) for data storage and processing Familiarity with React or similar front-end frameworks Experience with multimedia codecs and formats"

job_info = extract_job_info(job_desc)
print(job_info)
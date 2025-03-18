# Get Score For Your Resume:

Get your resume's score based on job description and find out how much you stand out with the help of the AI!

This project is using Random Forest Regressor to give you the score by matching your resume with job description based on 3 main criterias:
 1. Skills
 2. Experience
 3. Location

It matches skills using cosine similarity by converting skills into vectors with the help of TF-IDF. Then it compares whether you are in the same country as of the job's posting. Finally, it checks whether you belong to the experience range criteria. Then it calcuates the score!

I have used Next.js for the front-end development and Flask for the backend. This model gives scores in real-time so no databased is used. In future, I can add authentication too!

Below are some images of the projects!

# Images:

![1](https://github.com/user-attachments/assets/02d805d4-66c8-413e-96a8-a1af9663855a)

![2](https://github.com/user-attachments/assets/9d430c33-da27-48db-b896-63e8a110b62e)

![3](https://github.com/user-attachments/assets/c2c805d3-0f11-4ed1-b957-6c6a2516d5ea)

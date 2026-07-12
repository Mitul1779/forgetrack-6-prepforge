# PrepForge - AI-Powered Resume Review Assistant

PrepForge is a Flask-based web application that helps users improve their resumes using Google's Gemini AI. Users can upload a PDF resume, and the application extracts the text, analyzes it using Gemini 2.5 Flash, and generates detailed feedback with strengths, weaknesses, ATS improvement suggestions, missing skills, and an overall rating.

This project was built as the final project for the SAE DTU x ForgeTrack Python Track.

---

## Features

- Upload resume in PDF format
- Extract text using pdfplumber
- AI-powered resume analysis using Gemini 2.5 Flash
- ATS improvement suggestions
- Resume strengths and weaknesses
- Missing skills identification
- Overall resume rating
- Error handling for invalid or empty PDFs
- Responsive user interface built with Flask templates

---

## Tech Stack

- Python
- Flask
- Google Gemini 2.5 Flash API
- pdfplumber
- HTML
- CSS
- Markdown

---

## Installation

Clone the repository

```bash
git clone <repository-url>
cd PrepForge
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file using `.env.example`

```env
GEMINI_API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here
```

---

## Running the Project

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## Screenshots

### Home Page

<img width="1839" height="850" alt="Screenshot 2026-07-12 151136" src="https://github.com/user-attachments/assets/21591655-aaff-4134-8f97-41288b5ab1c7" />


---

### Upload Resume

<img width="1849" height="851" alt="Screenshot 2026-07-12 151317" src="https://github.com/user-attachments/assets/7506e3d4-21ec-4323-bfa8-e77d513260bc" />


---

### Resume Analysis

<img width="1837" height="850" alt="Screenshot 2026-07-12 151403" src="https://github.com/user-attachments/assets/59d7ffa1-6e16-4499-84d0-1ad67bcc3ee7" />


---

### Error Handling

<img width="1854" height="853" alt="Screenshot 2026-07-12 151415" src="https://github.com/user-attachments/assets/f3894719-5179-4759-9805-027fb00e80a8" />


---

## How It Works

1. User uploads a PDF resume.
2. Flask validates the uploaded file.
3. The resume is temporarily saved.
4. pdfplumber extracts text from the PDF.
5. The extracted text is sent to Gemini 2.5 Flash.
6. Gemini returns structured resume feedback.
7. Markdown is converted into HTML.
8. The formatted analysis is displayed to the user.
9. The uploaded PDF is deleted after processing.

---

## Future Improvements

- Job Description matching
- AI-generated interview questions
- Resume history
- User authentication
- Dashboard with previous analyses
- Structured JSON responses from Gemini
- Support for DOCX resumes

---

## Learning Outcomes

This project helped me learn and apply:

- Flask routing
- Template inheritance
- File uploads
- PDF parsing
- API integration
- Prompt engineering
- Environment variables
- Error handling
- Frontend integration with Flask

---

## Acknowledgements

- Google Gemini API
- Flask
- pdfplumber
- SAE DTU
- ForgeTrack

---

# Reflection

There are also a few of features that would be great to include if I had more time: I could compare the interview question responses to job descriptions, I would create an interview questions list directly from a job description, or I would parse the Gemini API output into a JSON object. What I can now state confidently that I'm able to do is, from an application scratch, design, build, and deploy a full application using the flask frameworks that incorporates routing, templating inheritance, file upload feature, interaction with external API's, managing env variables, handling application errors and debugging the issues in the same. it was more than just reading through the individual components tutorials - it was the way they interacted and fit together and i think i'm now confident to do anything more advanced from this type of python project.  

With more time I could have added a feature that would have compared the interview questions to job description or generated an interview question list based on the job description, or I would have processed the output of the Gemini API to be a JSON object instead of markdown. I would have also spiffied up the UI and added a database to save the old resume results.  

The most important takeaway from this project was confidence. Now, I can say with confidence that I can build an entire Flask application from the ground up - including routing, template inheritance, file uploads, integration of third party API’s, using environment variables, deploying the application, and debugging errors. It was more than simply reading the tutorials for each component individually - it was seeing how they spoke to each other that made it click, and now I feel ready to tackle any further, more advanced full-stack python projects! 
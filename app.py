from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from werkzeug.utils import secure_filename
from markdown import markdown
import os
from utils.parser import extract_pdf_text
from utils.gemini import analyze_resume

app = Flask(__name__)
app.config.from_object(Config)
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files.get("resume")
        if file and file.filename.lower().endswith(".pdf"):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            try:
                resume_text = extract_pdf_text(filepath)
                if not resume_text.strip():
                    raise ValueError("The uploaded PDF does not contain any extractable text.")
                analysis = analyze_resume(resume_text)
            except Exception as e:
                app.logger.exception(e)
                return render_template("error.html", message="Error processing the resume! Please ensure the PDF is valid and try again.")
            finally:
                if os.path.exists(filepath):
                    os.remove(filepath)
            analysis_html = markdown(analysis)
            return render_template("analysis.html", analysis=analysis_html)
        else:
            flash("Please upload a valid PDF file.", "error")
            return redirect(url_for("upload"))

    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)


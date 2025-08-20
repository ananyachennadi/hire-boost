from flask import Flask, render_template, request
from api.llm_client import optimise_cv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/optimise', methods=['POST'])
def optimise():
    cv_file = request.files.get('cv_file')
    file_bytes = cv_file.read()
    job_desc = request.form.get('job_desc')
    result = optimise_cv(file_bytes, job_desc)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
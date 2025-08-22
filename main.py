from flask import Flask, render_template, request, jsonify
from api.llm_client import optimise_cv

app = Flask(__name__)

# Define the route for the home page
# Triggered when the user navigates to the base URL
@app.route('/')
def index():
    return render_template('index.html')

# This route only accepts POST requests from the form submission.
@app.route('/optimise', methods=['POST'])
def optimise():
    # Extract the uploaded CV file from the request.
    cv_file = request.files.get('cv_file')
    file_bytes = cv_file.read()

    # Extract the job description from the form. 
    job_desc = request.form.get('job_desc')
    
    result = optimise_cv(job_desc, file_bytes)
    return jsonify({'result': result}) 
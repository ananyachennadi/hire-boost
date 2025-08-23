import os
from flask import Flask, render_template, request, jsonify
from api.llm_client import optimise_cv
from werkzeug.exceptions import RequestEntityTooLarge # Import RequestEntityTooLarge

app = Flask(__name__)

# Set a file size limit (e.g., 1 MB for free tiers to prevent memory issues)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024 

# Triggered when the user navigates to the base URL
@app.route('/')
def index():
    return render_template('index.html')

# This route only accepts POST requests from the form submission.
@app.route('/optimise', methods=['POST'])
def optimise():
    # Basic input validation
    if 'cv_file' not in request.files or not request.form.get('job_desc'):
        return jsonify({'error': 'Missing CV file or job description.'}), 400

    cv_file = request.files.get('cv_file')
    job_desc = request.form.get('job_desc')
    
    # Check for empty file
    if cv_file.filename == '':
        return jsonify({'error': 'No file selected.'}), 400

    try:
        # Check file extension
        if not cv_file.filename.endswith('.pdf'):
            return jsonify({'error': 'Invalid file type. Please upload a PDF.'}), 400
        
        # Read the file's content into memory. This is okay after size validation.
        file_bytes = cv_file.read()

        # Call the external function to process the data
        result = optimise_cv(job_desc, file_bytes)

        # Return the success response
        return jsonify({'result': result})

    except Exception as e:
        # Log the error for debugging purposes
        print(f"An error occurred: {e}")
        return jsonify({'error': 'An error occurred. Please try again.'}), 500

# Error handler for files exceeding the MAX_CONTENT_LENGTH
@app.errorhandler(RequestEntityTooLarge)
def handle_file_size_limit(error):
    # This message will be returned when a file larger than 1MB is uploaded
    return "The CV file is too large. Please upload a PDF under 1 MB.", 413
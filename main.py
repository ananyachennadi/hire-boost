from flask import Flask, render_template, request, jsonify
from api.llm_client import optimise_cv
from werkzeug.exceptions import RequestEntityTooLarge
import tempfile  # <-- Import the tempfile library
import os      # <-- Import the os library

app = Flask(__name__)

# 1MB file size limit to prevent memory issues
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

    # Create a temporary file to save the CV
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
    temp_file.close() # <-- Must close the handle to save the file
    
    try:
        # Check file extension
        if not cv_file.filename.endswith('.pdf'):
            return jsonify({'error': 'Invalid file type. Please upload a PDF.'}), 400
        
        # Save the uploaded file to the temporary disk location
        cv_file.save(temp_file.name)

        # Call the external function to process the data, passing the file path
        result = optimise_cv(job_desc, temp_file.name)

        # Return the success response
        return jsonify({'result': result})

    except Exception as e:
        # Log the error for debugging purposes
        print(f"An error occurred: {e}")
        return jsonify({'error': 'An error occurred. Please try again.'}), 500
    
    finally:
        # Ensure the temporary file is deleted, regardless of whether an error occurred
        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)

# Error handler for files exceeding the MAX_CONTENT_LENGTH
@app.errorhandler(RequestEntityTooLarge)
def handle_file_size_limit(error):
    # This message will be returned when a file larger than 1MB is uploaded
    return "The CV file is too large. Please upload a PDF under 1 MB.", 413
document.addEventListener('DOMContentLoaded', () => {

  // get references to important elements
  const dropArea = document.getElementById('drop-area');
  const fileInput = document.querySelector('#drop-area input[type="file"]');
  const form = document.getElementById('optimise-form'); 
  const resultDiv = document.getElementById('result-output');
  const submitButton = form.querySelector('.submit-button'); 

  // Prevent default behavior for drag and drop
  ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false);
  });

  function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
  }

  // Highlight drop area when a file is dragged over it
  ['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, () => {
      dropArea.classList.add('highlight');
    }, false);
  });

  // Remove highlight when the file is dragged away or dropped
  ['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, () => {
      dropArea.classList.remove('highlight');
    }, false);
  });

  // Handle the dropped files
  dropArea.addEventListener('drop', (e) => {
    const dt = e.dataTransfer;
    const files = dt.files;
    
    // Assign the dropped files to the file input
    fileInput.files = files; 

    handleFiles(files);
  }, false);

  // Handle files selected via the input
  fileInput.addEventListener('change', () => {
    handleFiles(fileInput.files);
  });

  function handleFiles(files) {
    if (files.length > 0) {
      const fileName = files[0].name;
      const uploadText = document.querySelector('.upload-text');
      uploadText.textContent = `${fileName} is ready to be optimised!`;
    }
  }

  form.addEventListener('submit', async (e) => {
      e.preventDefault(); // Stop the form from submitting normally
      
      const formData = new FormData(form);
      submitButton.disabled = true;
      submitButton.textContent = "Optimising...";
      
      try {
          // Show a loading state and disable submit button to stop spaming requests
          resultDiv.innerHTML = '<p>Optimising your CV...</p>';

          const response = await fetch('/optimise', {
              method: 'POST',
              body: formData
          });

          if (!response.ok) {
              throw new Error(`HTTP error! status: ${response.status}`);
          }

          const data = await response.json();
          
          if (data.result) {
              // Clear the loading message
              resultDiv.innerHTML = ''; 

              // Create a heading
              const heading = document.createElement('h2');
              heading.textContent = 'Optimised CV Output:';
              resultDiv.appendChild(heading);

              // Parse and inject the Markdown
              const parsedMarkdown = marked.parse(data.result);
              const contentDiv = document.createElement('div');
              contentDiv.innerHTML = parsedMarkdown;
              resultDiv.appendChild(contentDiv);

          } else {
              resultDiv.innerHTML = '<p>No result was returned.</p>';
          }

      } catch (error) {
          console.error('Error:', error);
          resultDiv.innerHTML = '<p>An error occurred. Please try again.</p>';
      } finally {
        // button re-enabled after finishing
        submitButton.disabled = false;
      }
  });

});
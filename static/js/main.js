document.addEventListener('DOMContentLoaded', () => {

  // get references to important elements
  const form = document.getElementById('optimise-form');
  const resultDiv = document.getElementById('result-output');
  const submitButton = form.querySelector('.submit-button');
  const notificationBar = document.getElementById('notification-bar');
  const notificationIcon = document.getElementById('notification-icon');
  const notificationText = document.getElementById('notification-text');
  const dropArea = document.getElementById('drop-area');
  const fileInput = document.querySelector('#drop-area input[type="file"]');
  const loadingScreen = document.getElementById('loading-screen');
  const mainContent = document.getElementById('main-content-wrapper');

  //store the original page title
  const originalTitle = document.title;
  
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

  // function that shows notification and message based on the result
  function showNotification(message, isSuccess) {
        notificationText.textContent = message;
        
        if (isSuccess) {
            notificationIcon.innerHTML = '<i class="fa-solid fa-check"></i>';
        } else {
            notificationIcon.innerHTML = '<i class="fa-solid fa-xmark"></i>';
        }
        
        notificationBar.style.display = 'flex';
    }

     // Function to hide the notification
    function hideNotification() {
        notificationBar.style.display = 'none';
    }

  //reset the title when the user focuses on the tab again
  window.addEventListener('focus', () => {
      document.title = originalTitle;
  });

  form.addEventListener('submit', async (e) => {
      e.preventDefault();
      
      const formData = new FormData(form);

      // hide any previous notifications
      // Show loading screen and hide main content
      loadingScreen.classList.remove('hidden-loading');
      mainContent.classList.add('hidden-loading');
      submitButton.disabled = true;
      resultDiv.innerHTML = '';
      hideNotification();

      try {
          const response = await fetch('/optimise', {
              method: 'POST',
              body: formData
          });

          if (!response.ok) {
              throw new Error(`HTTP error! status: ${response.status}`);
          }

          const data = await response.json();
          
          if (data.result) {
            //success: api returned a result
            showNotification("Optimised CV successfully generated", true);
            // change title on success
            document.title = 'Ready! ✅'

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
            // failure: api returned an empty result
            showNotification('An error occured: No result was returned', false);
              resultDiv.innerHTML = '<p>No result was returned.</p>';
            //Change title on failure
            document.title = 'Failed! ❌';
          }

      } catch (error) {
          console.error('Error:', error);
          resultDiv.innerHTML = '<p>An error occurred. Please try again.</p>';
          showNotification('An error occurred. Please try again', false);
          //Change title on error
          document.title = 'Failed! ❌'
      } finally {
        // button re-enabled after finishing
        submitButton.disabled = false;
        // Hide loading screen and show main content
        loadingScreen.classList.add('hidden-loading');
        mainContent.classList.remove('hidden-loading');
      }
  });

});
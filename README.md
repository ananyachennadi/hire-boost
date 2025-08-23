![GitHub License](https://img.shields.io/github/license/ananyachennadi/cv-optimiser?refresh=1)
# HireBoost
Automatically customise your CV for any job application with AI-powered matching and improvement suggestions.

---

## About

**HireBoost** is your final check before applying. This AI-powered tool helps you get your CV past automated filters and into the hands of a hiring manager.  
Stop wasting hours tweaking your CV for every job. Let AI do the hard work so you can focus on landing your next interview.

***

## Key Features

* **✅ Tailored CV:** Receive an optimised version of your CV, tailored to match a specific job description.
* **📈 Match Score:** Get an instant score (0-100) to see how well your CV matches the role.
* **🔍 Actionable Feedback:** Instantly see what keywords you're missing and get clear, specific suggestions for improvement.
* **💡 ATS Analysis:** See a breakdown of your strengths and how they align with the job description.

***

## Live Demo

See a full walkthrough of the application below.

![HireBoost App Demo](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2lnbnp1aThuZXNzbmJiNjA3NnZyYm5lMzFta2N1cnZjZWp5OGl0NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pe2DQ23sNxFMb6yRrz/giphy.gif)


**Try the app live on Render!**
* [https://hire-boost.onrender.com/]

--- 

## Technologies Used

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python, Flask
* **Deployment:** Render, Git, GitHub
* **APIs:** Google Generative AI (gemini-2.5-flash)

---

## Getting Started (Local Setup)

To run **HireBoost** on your machine, just follow these steps.

1.  **Clone the Repository**
    Start by cloning the project from GitHub and moving into the project directory.

    ```bash
    git clone [https://github.com/ananyachennadi/cv-optimiser.git](https://github.com/ananyachennadi/cv-optimiser.git)
    cd cv-optimiser
    ```

2.  **Set Up Your Environment**
    Next, create and activate a virtual environment to manage dependencies, then install the required packages.

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Add Your API Key**
    Create a new file called `.env` in the project's root directory and add your API key to it.

    ```
    GEMINI_API_KEY=your_api_key_here
    ```

4.  **Run the Application**
    Finally, use the `flask run` command to start the local server. The app will be running at `http://127.0.0.1:5000`. 🚀

    ```bash
    flask run
    ```

---
## Future Improvements
- [ ] Add a nicer loading state
- [ ] Implement a download option for the optimised CV

---
## Contact
If you have any questions or want to connect, feel free to reach out to me!
- LinkedIn: [www.linkedin.com/in/ananyachennadi]
- Email: [ananyachennadi2@gmail.com]

---
## Licence

This project is licensed under the **MIT License**.

For more information, see the `LICENSE` file in the repository.



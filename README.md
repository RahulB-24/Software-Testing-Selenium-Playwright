# Software Testing Assignment

This project contains automated test scripts for **login** and **registration modules** using **Selenium** and **Playwright**. It also generates **HTML test reports** for validation. The project is designed to be easily cloned and executed using **VS Code** or any Python environment.

---

## Demo Websites

1. **Login Module:** [The Internet Login Page](https://the-internet.herokuapp.com/login)  
2. **Registration Form:** [DemoQA Automation Practice Form](https://demoqa.com/automation-practice-form)

---

## Project Structure

software-testing-assignment/
│
├─ selenium_tests/ # Selenium test scripts
│ ├─ test_login.py
│ └─ test_registration.py
│
├─ playwright_tests/ # Playwright test scripts
│ ├─ test_login.py
│ └─ test_registration.py
│
├─ reports/ # HTML reports
│ ├─ selenium_report.html
│ └─ playwright_report.html
│
├─ requirements.txt # Python dependencies
├─ README.md # Project documentation
└─ .gitignore # Exclude venv, pycache, reports

yaml
Copy code

---

## Prerequisites

- Python 3.10 or higher installed  
- VS Code or any IDE  
- Git (for version control)  

---

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/software-testing-assignment.git
cd software-testing-assignment
Create a virtual environment

bash
Copy code
python -m venv venv
Activate the virtual environment

Windows:

bash
Copy code
venv\Scripts\activate
Mac/Linux:

bash
Copy code
source venv/bin/activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Install Playwright browsers

bash
Copy code
playwright install
Running Tests
Selenium Tests
bash
Copy code
pytest selenium_tests/ --html=reports/selenium_report.html --self-contained-html -v
Playwright Tests
bash
Copy code
pytest playwright_tests/ --html=reports/playwright_report.html --self-contained-html -v
Notes:

-v enables verbose output

--self-contained-html creates a report with embedded CSS/JS for easy sharing

Test Cases
Login Module
Valid Login: Enter valid credentials → user redirected to /secure page.

Invalid Login: Enter invalid credentials → error message appears: "Your username is invalid!"

Registration Form
Fill out form (First Name, Last Name, Email, Gender, Mobile Number) → click Submit → confirmation modal appears.

Viewing Test Reports
After running the tests, open the HTML files in the reports/ folder using any browser:

Selenium Report: reports/selenium_report.html

Playwright Report: reports/playwright_report.html

Recommended Best Practices
Keep the virtual environment active when running tests.

Update requirements.txt if new packages are added.

Ensure internet connectivity for accessing demo websites.
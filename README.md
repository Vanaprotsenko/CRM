    CRM Application

Description
This project is a client management system (CRM) developed using Django. It allows users to manage goods and track user actions through a logsystem.

Installation

1. Cloning of the repository:
   git clone https://github.com/Vanaprotsenko/CRM.git
   cd your_project_directory

2. Creating a virtual environment:
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv Scripts activate  # For Windows

3. Setting dependencies:
   pip install -r requirements.txt

4. Application of migration:
   python manage.py migrate

5. Server start:
   python manage.py runserver

Use
- Go to the browser at http://127.0.0.1:8000/auth/ for login.
- Depending on your role (administrator, manager, user) you will be able to add, edit or remove items.

Logsystem
Added logsystem to record user actions. Logs are written to the app.log file and include information about actions such as successful or unsuccessful user logins, adding, updating, and removing products.

Log format
Log entries have the following format:
%(asctime)s - %(levelname)s - %(message)s

Testing
- To test the application functions, perform:
  python manage.py test
- The logsystem tests verify the correctness of the entries.

Documentation
For more information, please refer to the code or documentation of the libraries used in the project.

Remark
- Make sure you have Python and Django installed, as well as other required libraries from requirements.txt.

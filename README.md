# To setup FLASK

---

## For Linux based Environment

1. Create a folder into your machine and open it in code editor.
2. Create a venv using `python3 -m venv venv_name` and activate it using `source flask_venv/bin/activate`.
3. Create app.py and refere to the it.
4. To setup developmet not to run **flask run** for everytime we make changes to see in the browser use
   `export FLASK_APP=app` and `export FLASK_ENV=development` by creating environmet variable. Here, we created as development.
5. Flask run or python app.py if debug is set explicitly
6. To prevent creating **pycache** file use
   `export PYTHONDONTWRITEBYTECODE=1`.

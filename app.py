# app.py
from flask import Flask, request, render_template

app = Flask(__name__)

# Security Vulnerability: Lack of Input Validation
@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    # Vulnerable: No input validation or sanitation
    return f'Hello, {username}! Your password is: {password}'

# Security Vulnerability: SQL Injection
@app.route('/search')
def search():
    query = request.args.get('query')
    # Vulnerable: SQL Injection
    result = db.execute(f"SELECT * FROM products WHERE name = '{query}'")
    return render_template('search_results.html', result=result)

# Code Quality Issue: Unused Variable
@app.route('/unused')
def unused_variable():
    variable = 'This variable is not used.'
    return 'Unused Variable Example'

if __name__ == '__main__':
    app.run()

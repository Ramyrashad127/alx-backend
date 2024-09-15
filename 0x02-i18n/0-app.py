#!/usr/bin/env python3


"""import modules"""
from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def hmoe():
    """diplay home page"""
    return render_template('0-index.html')

if __name__ == "__main__":
    app.run(debug=True)
"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from SOFT_ENG_SV_MAP import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index1.html',
        title='First floor',
        year=datetime.now().year,
    )


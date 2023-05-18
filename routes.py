"""
Routes and views for the bottle application.
"""
import json
from bottle import route, view, template
from datetime import datetime
from bottle import post, request

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )


@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )
@route('/reviews')
@view('reviews')
def reviews():
    return template('reviews', title='Reviews', message='Give your review or watch other reviews',
    userreviews="",year=datetime.now().year)

import re
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mail import Message
from portfolio import app,mail


@app.route('/', methods=['GET','POST'])
def landing():
    if request.method=='POST':

        name=request.form.get('name')
        email=request.form.get('email')
        message=request.form.get('message')

        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        
        if not name or not email:

            flash('Please Name and Email fields cannot be empty', 'error')
            return redirect(url_for('home') + '#contact-section')
        
        elif not re.match(email_regex,email):
            flash ('Please fill in a valid email address','error')
            return redirect(url_for('home') + '#contact-section')
        else:
            my_email = "oayomideg@gmail.com"
            msg = Message(
                subject="New Portfolio Contact Me Form Submission",
                sender=app.config['MAIL_DEFAULT_SENDER'],
                recipients=[my_email]
            )
            msg.html= f"""
            <h3 style='color:white; background-color:blue; text-align:center; padding:20px 5px;'> You have a new message from the contact form</h3>
            <p> Name: {name} </p>
            <p> Email: {email} </p>
            
            Message:
            {message}
            """
            try:
                mail.send(msg)
                flash('Your message has been sent successfully!', 'success')
                return redirect(url_for('home') + '#contact-section')
            except Exception as e:
                flash('There was an issue sending your message. Please try again.', 'error')
                print(f"Email send error: {e}")
                return redirect(url_for('home') + '#contact-section')
    return render_template('index.html')



@app.route('/home/', methods=['GET','POST'])
def home():
    if request.method=='POST':

        name=request.form.get('name')
        email=request.form.get('email')
        message=request.form.get('message')

        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        
        if not name or not email:

            flash('Please Name and Email fields cannot be empty', 'error')
            return redirect(url_for('home') + '#contact-section')
        
        elif not re.match(email_regex,email):
            flash ('Please fill in a valid email address','error')
            return redirect(url_for('home') + '#contact-section')
        else:
            my_email = "oayomideg@gmail.com"
            msg = Message(
                subject="New Portfolio Contact Me Form Submission",
                sender=app.config['MAIL_DEFAULT_SENDER'],
                recipients=[my_email]
            )
            msg.html= f"""
            <h3 style='color:white; background-color:blue; text-align:center; padding:20px 5px;'> You have a new message from the contact form</h3>
            <p> Name: {name} </p>
            <p> Email: {email} </p>
            
            Message:
            {message}
            """
            try:
                mail.send(msg)
                flash('Your message has been sent successfully!', 'success')
                return redirect(url_for('home') + '#contact-section')
            except Exception as e:
                flash('There was an issue sending your message. Please try again.', 'error')
                print(f"Email send error: {e}")
                return redirect(url_for('home') + '#contact-section')
    return render_template('index.html')



@app.route('/resume/')
def resume():
    return render_template('resume.html')
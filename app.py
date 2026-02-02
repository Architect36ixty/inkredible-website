from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_unsafe_key_for_dev')

# Flask-Mail Configuration for Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
# Default sender and recipient
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')
MAIL_RECIPIENT = os.environ.get('MAIL_USERNAME') # Send emails to yourself

mail = Mail(app)

# Inject current date time into all templates for the footer
@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    # Placeholder data for the team
    team_members = [
        {'name': 'Alex Johnson', 'role': 'Lead Architect', 'bio': 'Master of Python and scalable systems.', 'img': 'team_member_1.jpg'},
        {'name': 'Maria Rodriguez', 'role': 'Frontend Specialist', 'bio': 'Turning complex UIs into smooth experiences.', 'img': 'team_member_2.jpg'},
        {'name': 'David Kim', 'role': 'Backend Developer', 'bio': 'Database wizard and API expert.', 'img': 'team_member_3.jpg'},
        {'name': 'Sarah Jenkins', 'role': 'Project Manager', 'bio': 'Keeping projects on track and clients happy.', 'img': 'team_member_4.jpg'},
    ]
    return render_template('team.html', team=team_members)

@app.route('/consulting')
def consulting():
    return render_template('consulting.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message_body = request.form.get('message')

        if not name or not email or not message_body:
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('contact'))

        msg = Message(subject=f"New Inquiry from {name} via Inkredible Website",
                      recipients=[MAIL_RECIPIENT])
        msg.body = f"""
Name: {name}
Email: {email}

Message:
{message_body}
        """
        try:
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            print(f"Error sending email: {e}")
            flash('There was an error sending your message. Please try again later.', 'error')
            return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    # Only run debug mode locally
    app.run(debug=True)

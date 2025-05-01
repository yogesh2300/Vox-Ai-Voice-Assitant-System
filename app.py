import google.generativeai as genai
import os
from flask import Flask, render_template, request, jsonify, redirect, session
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from difflib import SequenceMatcher

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'


class User( db.Model ):
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String( 100 ), nullable=False )
    email = db.Column( db.String( 100 ), unique=True )
    password = db.Column( db.String( 100 ) )

    def __init__(self, email, password, name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw( password.encode( 'utf-8' ), bcrypt.gensalt() ).decode( 'utf-8' )

    def check_password(self, password):
        return bcrypt.checkpw( password.encode( 'utf-8' ), self.password.encode( 'utf-8' ) )


with app.app_context():
    db.create_all()

# Set your Google API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAKKhp8s7h-fu_muzQN21zC-FdEpKYKRZk"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("models/gemini-1.5-pro")

# Global variables to store conversation history and context
conversation_history = []

# Voice assistance function with enhanced topic management
def voice_assistance(user_input):
    global conversation_history

    # Improved prompt with focus on concise and direct answers
    prompt = f"""
    You are an AI assistant in an engaging conversation with a user. The user just asked the following question:
    '{user_input}'
    Provide a direct and informative answer, focusing on the exact details the user is asking for. Avoid unnecessary elaboration or asking follow-up questions unless essential to the user’s inquiry. Keep the response clear, concise, and to the point. If the topic is complex, briefly summarize the key aspects.
    """

    response = model.generate_content(prompt).text

    # Update conversation history
    conversation_history.append({
        'user': user_input,
        'ai': response
    })

    return response


# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/help')
def help():
    return render_template('help.html')



# Route to handle voice input and return model response with conversation history
@app.route('/process_voice', methods=['POST'])
def process_voice():
    user_input = request.json.get("user_input")
    response = voice_assistance(user_input)

    # Return the updated conversation history
    return jsonify({'response': response, 'conversation_history': conversation_history})

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # handle request
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        new_user = User(name=name,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')



    return render_template('register.html')


@app.route( '/login', methods=['GET', 'POST'] )
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by( email=email ).first()

        if user and user.check_password( password ):
            session['email'] = user.email
            return redirect( '/' )
        else:
            return render_template( 'login.html', error='Invalid user' )

    return render_template( 'login.html' )


@app.route( '/dashboard' )
def dashboard():
    if session['email']:
        user = User.query.filter_by( email=session['email'] ).first()
        return render_template( 'dashboard.html', user=user )

    return redirect( '/login' )

@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
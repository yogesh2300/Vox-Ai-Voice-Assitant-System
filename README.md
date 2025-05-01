🎙️ VOXAI — Voice Assistant Web App with Gemini AI
VOXAI is an intelligent, voice-based assistant web application powered by Google's Gemini 1.5 Pro model. It offers real-time AI-driven responses to user voice queries and provides a seamless conversational experience. Users can register, log in, and interact with the assistant via a clean Flask-based interface.

🚀 Features
🔐 User Registration and Authentication using Flask & SQLite

🤖 Voice-powered AI Assistant with Google Gemini

💬 Maintains conversational history

🌐 Flask web app structure with routes for /, /login, /register, /dashboard, and more

🛡️ Passwords securely hashed using bcrypt

🗃️ Stores user data with SQLAlchemy ORM

🧠 Tech Stack
Backend: Python, Flask, SQLAlchemy

AI Model: Google Gemini 1.5 Pro via google.generativeai

Database: SQLite

Security: bcrypt for password hashing

Frontend: HTML (via Flask templates)

🛠️ Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/voxai.git
cd voxai
Create and activate a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up your environment

Replace GOOGLE_API_KEY with your actual Google Gemini API key.

You can store it in an .env file or export it:

bash
Copy
Edit
export GOOGLE_API_KEY="your-api-key"
Run the app

bash
Copy
Edit
python app.py
Navigate to

cpp
Copy
Edit
http://127.0.0.1:5000/
🗂️ Project Structure
csharp
Copy
Edit
.
├── app.py                  # Main Flask application
├── templates/              # HTML templates (index, login, register, etc.)
├── static/                 # Static assets (CSS, JS, media)
├── database.db             # SQLite database
└── README.md
📌 Routes
Route	Description
/	Homepage
/register	User registration
/login	User login
/dashboard	Personalized user dashboard
/process_voice	POST route for handling voice AI
/logout	User logout

📎 Future Enhancements
🎤 Integrate real-time voice-to-text conversion

🧠 Context-aware responses with advanced memory handling

📱 Mobile-responsive UI

☁️ Deploy on platforms like Heroku or Azure

📃 License
This project is licensed under the MIT License - see the LICENSE file for details.

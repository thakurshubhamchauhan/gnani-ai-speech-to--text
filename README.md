# Gnani AI Speech-to-Text

A Django web application that converts audio speech into text using the Gnani AI / Vachana API.

## Features
- Audio file upload
- Speech-to-text conversion
- Hindi speech recognition
- Django web interface

## Technologies
- Python
- Django
- HTML and CSS
- Requests
- Python dotenv
- Gnani AI API

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/thakurshubhamchauhan/gnani-ai-speech-to--text.git
cd gnani-ai-speech-to--text
```

### 2. Install dependencies
```bash
python -m pip install django requests python-dotenv
```

### 3. Configure API key
Create a `.env` file in the project root:

```env
GNANI_API_KEY=your_api_key_here
```

Replace the placeholder with your own API key. Never upload your real API key to GitHub.

### 4. Run the project
```bash
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Author
Shubham Chauhan

GitHub: https://github.com/thakurshubhamchauhan
phone_number:9027173541
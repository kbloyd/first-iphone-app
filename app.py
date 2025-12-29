"""
Magic Decision Maker - A fun interactive web app for making decisions
"""
import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Magic responses
RESPONSES = [
    "Yes, definitely!",
    "It is certain!",
    "Without a doubt!",
    "You may rely on it!",
    "As I see it, yes!",
    "Most likely!",
    "Outlook good!",
    "Signs point to yes!",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]

COLORS = [
    "#9b59b6",  # Purple
    "#3498db",  # Blue
    "#e74c3c",  # Red
    "#2ecc71",  # Green
    "#f39c12",  # Orange
    "#1abc9c",  # Turquoise
]


@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/api/decision')
def get_decision():
    """Return a random decision"""
    response = random.choice(RESPONSES)
    color = random.choice(COLORS)
    return jsonify({
        'response': response,
        'color': color
    })


@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

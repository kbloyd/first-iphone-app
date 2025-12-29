# 🔮 Magic Decision Maker

A fun, interactive web application that helps you make decisions! Built with Flask and featuring a beautiful mobile-friendly interface with animations.

## Features

- 🎱 Interactive magic 8-ball style decision maker
- 📱 Mobile-optimized with shake detection (on supported devices)
- 🎨 Beautiful animated UI with color-changing responses
- ✨ Smooth animations and particle effects
- 🧪 Comprehensive unit tests

## Screenshots

The app features a stunning purple gradient background with a magic 8-ball interface that responds to taps and shakes!

## Installation

### Prerequisites
- Python 3.12 or higher
- pip or uv package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/first-iphone-app.git
cd first-iphone-app
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the App

### On Your Computer

Start the Flask development server:
```bash
python app.py
```

Then open your browser to `http://localhost:5000`

### On Your iPhone

#### Option 1: Using Pythonista (iOS App)

1. Install [Pythonista 3](https://apps.apple.com/us/app/pythonista-3/id1085978097) from the App Store
2. Clone or download this repository to your iPhone
3. Open `app.py` in Pythonista
4. Install Flask using Pythonista's pip (Tools > Pip > Search for "flask")
5. Run the script
6. Open the local URL in Safari

#### Option 2: Access from Computer

1. Start the app on your computer (same network as iPhone)
2. Find your computer's local IP address:
   - Mac/Linux: `ifconfig | grep inet`
   - Windows: `ipconfig`
3. On your iPhone's Safari, go to `http://YOUR_IP_ADDRESS:5000`

#### Option 3: Deploy to a Server

Deploy to services like:
- Heroku
- Railway
- Render
- PythonAnywhere

Then access from anywhere on your iPhone!

## Running Tests

Run the unit tests with pytest:
```bash
pytest
```

For verbose output:
```bash
pytest -v
```

For coverage report:
```bash
pytest --cov=app tests/
```

## How to Use

1. Open the app in your browser
2. Think of a yes/no question
3. Either:
   - Tap the magic ball
   - Click the "Ask the Magic Ball" button
   - Shake your phone (on supported devices)
4. Watch the animation and receive your answer!

## API Endpoints

- `GET /` - Main application page
- `GET /api/decision` - Returns a random decision (JSON)
- `GET /api/health` - Health check endpoint (JSON)

### Example API Response

```json
{
  "response": "Yes, definitely!",
  "color": "#9b59b6"
}
```

## Project Structure

```
first-iphone-app/
├── app.py                 # Flask application
├── templates/
│   └── index.html        # Main HTML template with CSS/JS
├── tests/
│   ├── __init__.py
│   └── test_app.py       # Unit tests
├── requirements.txt       # Python dependencies
├── pyproject.toml        # Project metadata
└── README.md             # This file
```

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Testing**: pytest
- **Design**: Responsive mobile-first design

## Features Explained

### Shake Detection
The app uses the DeviceMotion API to detect when you shake your iPhone, automatically triggering a new decision.

### Animations
- Shake animation when activated
- Ripple effect on tap
- Smooth color transitions
- Floating particle effects in background

### Mobile Optimization
- Responsive design that works on all screen sizes
- Touch-optimized interactions
- iOS status bar integration
- Prevents zooming and scrolling for app-like experience

## Contributing

Feel free to fork this project and submit pull requests!

## License

MIT License - feel free to use this project however you'd like!

## Author

Created with ❤️ for making decisions more fun!

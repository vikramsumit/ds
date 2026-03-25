import os
import eventlet
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# Create Flask app and SocketIO instance
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
socketio = SocketIO(app, cors_allowed_origins="*")

# ---------------------------
# Routes
# ---------------------------
@app.route('/')
def index():
    """Serve the whiteboard page."""
    return render_template('index.html')

# ---------------------------
# SocketIO event handlers
# ---------------------------
@socketio.on('draw')
def handle_draw(data):
    """Broadcast drawing data to all connected clients except the sender."""
    emit('draw', data, broadcast=True, include_self=False)

@socketio.on('clear')
def handle_clear():
    """Broadcast a clear command to all clients."""
    emit('clear', broadcast=True)

if __name__ == '__main__':
    try:
        socketio.run(app, debug=True, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
    except ImportError as e:
        print("Missing dependencies. Install with:")
        print("pip install flask flask-socketio eventlet")
        print("Error:", e)
    except Exception as e:
        print("Error starting server:", e)


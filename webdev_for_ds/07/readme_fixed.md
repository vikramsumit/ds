"""
Real-time Collaborative Whiteboard ✨
======================================
A Flask + SocketIO web app where multiple users can draw together on the same canvas in real-time!

## 🚀 Features
- ✅ Real-time collaborative drawing (broadcast to all clients)
- 🎨 Color picker & brush size slider
- 🧹 Clear canvas (syncs across all users)
- 📱 Responsive UI + mobile touch support
- 🌐 Works across multiple browser tabs/devices

## ✅ Fixed Issues
- `render_template('index.html')` - added missing quotes (was SyntaxError)
- Added `eventlet` import for WebSocket support
- Error handling for missing dependencies
- Added `allow_unsafe_werkzeug=True` for development

## 🛠️ Setup & Run
```bash
cd 07
pip install flask flask-socketio eventlet
python main.py  # or python main_fixed.py
```

Open http://localhost:5000 in multiple tabs/browsers to test collaboration!

## 🧪 Test Steps
1. Start server: `python main.py`
2. Open 2+ browser tabs to http://localhost:5000
3. Draw in one tab → see strokes appear instantly in others
4. Change color/brush size → verify sync
5. Click Clear → all canvases clear simultaneously

## 📱 Mobile Testing
Open on phone/tablet (same network) → drawing works with touch!

---
**Status: Fixed & Ready to Demo! 🎉**
"""


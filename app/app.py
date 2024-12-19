from flask import Flask, render_template, Response
import camera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(camera.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Optional: Admin login and dashboard routes
@app.route('/admin')
def admin_dashboard():
    # Implement admin dashboard logic
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, Response, request, jsonify
from picamera2 import Picamera2 # Use the modern picamera2 library
import cv2
import lampControl
import mechanum # Import the entire mechanum module
import math
import time
import swivel

app = Flask(__name__)

# --- Robot State ---
# Store the current speed percentage, updated by the frontend slider.
current_speed_percent = 50
current_swivel_angle = 1500

# --- Camera Setup ---
# Initialize and configure the camera directly using picamera2
camera = Picamera2()
camera.configure(camera.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
camera.start()
# Give the camera a moment to warm up
time.sleep(1)

@app.route('/')
def index():
    """Renders the main control page."""
    return render_template('index.html')

def gen_frames():
    """Generates video frames with a speed overlay."""
    global current_speed_percent
    
    while True:
        # Capture a frame as a NumPy array
        frame = camera.capture_array()

        # --- Add Speed Overlay ---
        # Define text properties for the speed display
        speed_text = f"Speed: {current_speed_percent}%"
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.8
        color = (0, 255, 0) # Green color in BGR
        thickness = 2
        position = (15, 40) # Position on the frame (x, y)

        # Draw the text onto the frame
        cv2.putText(frame, speed_text, position, font, font_scale, color, thickness, cv2.LINE_AA)
        
        # Encode the frame in JPEG format
        ret, buffer = cv2.imencode(".jpg", frame)

        # Ensure the frame was successfully encoded
        if not ret:
            continue

        # Convert the buffer to bytes
        frame_bytes = buffer.tobytes()

        # Yield the output frame in the byte format for streaming
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route that calls the frame generator."""
    return Response(gen_frames(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/control', methods=['POST'])
def control():
    """Handles all robot control commands (movement, lights, etc.)."""
    global current_speed_percent
    data = request.get_json()
    command = data.get('command')
    value = data.get('value')

    print(f"Received command: {command}, value: {value}, speed: {current_speed_percent}%")

    # --- Speed Control ---
    if command == 'speed':
        current_speed_percent = int(value)
        print(f"Speed set to: {current_speed_percent}%")
    
    # --- Light Bar Control ---
    elif command == 'light_bar':
        if value == 'on':
            lampControl.lampOn(lampControl.LAMP_COLOR)
            print("Lamp turned ON")
        else:
            lampControl.lampOff()
            print("Lamp turned OFF")

    # --- Movement Control ---
    elif command == 'move':
        if value == 'forward':
            mechanum.moveForward(current_speed_percent)
            print("Moving forward")
        elif value == 'backward':
            mechanum.moveBackward(current_speed_percent)
            print("Moving backward")
        elif value == 'left':
            mechanum.moveLeft(current_speed_percent)
            print("Strafing left")
        elif value == 'right':
            mechanum.moveRight(current_speed_percent)
            print("Strafing right")
        elif value == 'stop':
            mechanum.stop()
            print("Movement stopped")

    # --- Turning Control ---
    elif command == 'turn':
        if value == 'left':
            mechanum.turn(-current_speed_percent)
            print("Turning left")
        elif value == 'right':
            mechanum.turn(current_speed_percent)
            print("Turning right")
        elif value == 'stop':
            mechanum.stop()
            print("Turning stopped")
            
    # --- Gimbal Control (Placeholder) ---
    elif command == 'gimbal':
        print(current_swivel_angle)
        if value == 'left':
            current_swivel_angle += 50
            if current_swivel_angle >= 2500:
                current_swivel_angle = 2500
                print("Cannot swivel further")
            else:
                print("Pivoting gimbal left")
                swivel.rotateCamera(current_swivel_angle,1)
                print("Pivoting gimbal left")
        elif value == 'right':
            current_swivel_angle -= 50
            if current_swivel_angle <= 500:
                current_swivel_angle = 500
                print("Cannot swivel further")
            else:
                print("Pivoting gimbal right")
                swivel.rotateCamera(current_swivel_angle,1)
                print("Pivoting gimbal right")
        elif value == 'stop':
            print("Gimbal stopped")

    return jsonify(status="success", command=command, value=value)

@app.route('/update_speed', methods=['POST'])
def update_speed():
    """Calculates and returns vehicle stats based on speed percentage."""
    data = request.get_json()
    speed_percent = int(data.get('speed'))

    # Calculate velocity, RPM, and FPS using mechanum functions
    fb_velocity = mechanum.sepVel(speed_percent)
    if fb_velocity is None:
        fb_velocity = 0

    rpm = mechanum.getRPM(fb_velocity)
    fps = fb_velocity / 304.8

    return jsonify(rpm=rpm, fps=fps)

if __name__ == '__main__':
    # Initialize the robot motor pins on startup
    try:
        mechanum.init()
        print("✓ Motor pins initialized successfully.")
    except Exception as e:
        print(f"⚠️ Could not initialize motor pins: {e}")
        print("Running in simulation mode without GPIO control.")

    # Run the Flask web server
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)

import os
import subprocess
import sys
import requests
from pyngrok import ngrok
from google.colab import userdata

def install_and_import(package):
    try:
        __import__(package)
        print(f'{package} is already installed.')
    except ImportError:
        print(f'{package} not found. Installing...')
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', package])
        print(f'{package} installed.')

# 1. Install necessary packages if they are not already installed
install_and_import('pyngrok')
install_and_import('requests')
install_and_import('streamlit')
install_and_import('streamlit_autorefresh')

# 2. Set up ngrok authentication token
NGROK_AUTH_TOKEN = userdata.get('NGROK_AUTH_TOKEN')
if not NGROK_AUTH_TOKEN:
    print("Error: NGROK_AUTH_TOKEN not found in Colab secrets. Please add it.")
    sys.exit(1)

ngrok.set_auth_token(NGROK_AUTH_TOKEN)

# 3. Define Streamlit app path and new port
APP_PATH = '/content/drive/MyDrive/project_cd/app/app.py'
PORT = 8502 # Changed port from 8501 to 8502

# 4. Start Streamlit server in the background
print("Starting Streamlit server...")
process = subprocess.Popen([sys.executable, '-m', 'streamlit', 'run', APP_PATH, '--server.port', str(PORT)],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Give Streamlit some time to start
import time
time.sleep(5) # Adjust based on your app's startup time

# Check if Streamlit started successfully
if process.poll() is not None and process.returncode != 0:
    stdout, stderr = process.communicate()
    print("Streamlit server failed to start.")
    print("STDOUT:", stdout)
    print("STDERR:", stderr)
    sys.exit(1)

print("Streamlit server is live ✅")

# 5. Start ngrok tunnel
print("Starting ngrok tunnel...")
tunnel = ngrok.connect(PORT)
public_url = tunnel.public_url

print(f"\n🌍 PUBLIC URL:\n{public_url}")
print(f"✅ ICTA Operations Platform Live")

# Keep the script running to maintain the tunnel and Streamlit app
# This loop will keep the ngrok tunnel and Streamlit app alive
# until you manually stop the cell execution.
try:
    while True:
        time.sleep(60)
except KeyboardInterrupt:
    print("\nShutting down ngrok tunnel and Streamlit server...")
    ngrok.kill()
    process.terminate()
    process.wait()
    print("Processes terminated.")
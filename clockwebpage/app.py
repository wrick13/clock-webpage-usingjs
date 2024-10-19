from flask import Flask
import os
import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    
    full_name = "Aritra Mukherjee"
    username = os.getlogin()

  
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')


    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

   
    return f"""
    <h1>System Info</h1>
    <p><b>Name:</b> {full_name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

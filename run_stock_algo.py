# /root/chitraksh/stock_market_breakout_7/run_all.py
import os
import subprocess
import time
from datetime import datetime
from dotenv import load_dotenv

# -------- CONFIG ---------
PROJECT_DIR = "/root/chitraksh/stock_market_breakout_7"
VENV_PYTHON = os.path.join(PROJECT_DIR, "stock_market_env/bin/python")
GET_ACCESS_SCRIPT = os.path.join(PROJECT_DIR, "access_token.py")
COLLECTOR_SCRIPT = os.path.join(PROJECT_DIR, "collector1.py")
SERVER_SCRIPT = os.path.join(PROJECT_DIR, "server30b.py")
LOG_DIR = os.path.join(PROJECT_DIR, "logs")

# -------- SETUP ----------
os.makedirs(LOG_DIR, exist_ok=True)
load_dotenv(os.path.join(PROJECT_DIR, ".env"))

print("📁 Changing directory to:", PROJECT_DIR)
os.chdir(PROJECT_DIR)

# -------- STEP 1: Always Generate New Access Token --------
print("\n🔑 Running access_token.py to generate a new access token...")
subprocess.run(f"{VENV_PYTHON} {GET_ACCESS_SCRIPT}", shell=True, executable="/bin/bash")

# -------- STEP 2: Start Collector & Server --------
print("\n🚀 Starting collector1.py and server30b.py in background...")

# Use timestamped log files (optional but recommended)
date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
collector_log = os.path.join(LOG_DIR, f"collector_{date_str}.log")
server_log = os.path.join(LOG_DIR, f"server_{date_str}.log")

collector_cmd = f"{VENV_PYTHON} {COLLECTOR_SCRIPT} >> {collector_log} 2>&1"
server_cmd = f"{VENV_PYTHON} {SERVER_SCRIPT} >> {server_log} 2>&1"

collector_proc = subprocess.Popen(collector_cmd, shell=True, executable="/bin/bash")
server_proc = subprocess.Popen(server_cmd, shell=True, executable="/bin/bash")

print(f"✅ Collector running with PID {collector_proc.pid}")
print(f"✅ Server running with PID {server_proc.pid}")
print(f"🧾 Logs are being saved to:")
print(f"   - {collector_log}")
print(f"   - {server_log}")

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    print("\n🛑 Stopping processes...")
    collector_proc.terminate()
    server_proc.terminate()
    print("✅ All stopped.")

import subprocess
import psutil
import time
import os

THRESHOLD_UP = 75
THRESHOLD_DOWN = 30
MAX_INSTANCES = 5
MIN_INSTANCES = 1

INSTANCE_GROUP = "auto-scale-group"
ZONE = "us-central1-c"



result = subprocess.getoutput(
    "gcloud compute instance-groups managed list-instances auto-scale-group --zone=us-central1-c --format='value(name)'"
)

current_size = len(result.splitlines())
print(f"✅ Detected current instances: {current_size}")

cooldown = 30   # seconds

while True:
    cpu = psutil.cpu_percent(interval=5)
    print(f"CPU Usage: {cpu}% | Instances: {current_size}")

    # 🔼 SCALE UP
    if cpu > THRESHOLD_UP and current_size < MAX_INSTANCES:
        current_size += 1
        print(f"🔥 Scaling UP to {current_size}")

        os.system(
            f"gcloud compute instance-groups managed resize {INSTANCE_GROUP} "
            f"--size={current_size} --zone={ZONE}"
        )

        print("⏳ Cooldown after scale-up...")
        time.sleep(cooldown)

    # 🔽 SCALE DOWN
    elif cpu < THRESHOLD_DOWN and current_size > MIN_INSTANCES:
        current_size -= 1
        print(f"⬇️ Scaling DOWN to {current_size}")

        os.system(
            f"gcloud compute instance-groups managed resize {INSTANCE_GROUP} "
            f"--size={current_size} --zone={ZONE}"
        )

        print("⏳ Cooldown after scale-down...")
        time.sleep(cooldown)

    time.sleep(5)

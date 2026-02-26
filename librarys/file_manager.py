import os
import time
import json
from datetime import datetime
#raboti se v C:\Users\samol\Desktop\New folder\New folder

CHECK_WINDOW_SEC = 30 * 60
SLEEP_INTERVAL = 10
LOG_PATH_THIS = "../modified.log"

def write_output(log_path, records):
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)

def main():
    root = input("Enter path to folder to monitor: ").strip()
    log_path = os.path.join(root, LOG_PATH_THIS)
    print(f"Monitoring: {root}")
    while True:
        now = time.time()
        cutoff = now - CHECK_WINDOW_SEC
        records = []
        for name in os.listdir(root):
            full = os.path.join(root, name)
            if not os.path.isfile(full):
                continue
            nowtime = os.path.getmtime(full)
            if nowtime >= cutoff:
                htime = datetime.fromtimestamp(nowtime).isoformat()
                records.append({"path": name, "time of change": htime})
        write_output(log_path, records)
        time.sleep(SLEEP_INTERVAL)

if __name__ == "__main__":
    main()
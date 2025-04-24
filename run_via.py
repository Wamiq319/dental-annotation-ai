import os
import subprocess
import webbrowser
import time

# --- Paths ---
base_dir = os.path.dirname(os.path.abspath(__file__))
raw_dir = os.path.join(base_dir, 'data', 'raw')
processed_dir = os.path.join(base_dir, 'data', 'processed')
annotated_dir = os.path.join(base_dir, 'data', 'annotated')
json_dir = os.path.join(base_dir, 'data', 'annotations_json')

# --- Ensure dirs exist ---
for d in [raw_dir, processed_dir, annotated_dir, json_dir]:
    os.makedirs(d, exist_ok=True)

# --- Step 1: Preprocess images ---
def preprocess():
    from scripts import preprocess as p
    p.preprocess_all_images(raw_dir, processed_dir)

# --- Step 2: Annotate images ---
def annotate():
    from scripts import annotate as a
    a.annotate_all_images(processed_dir, annotated_dir, json_dir)

# --- Step 3: Start local server from root ---
def start_via():
    subprocess.Popen(["python", "-m", "http.server", "8001"], cwd=base_dir)
    time.sleep(2)
    webbrowser.open("http://localhost:8001/index.html")
    print(f"\n✅ VIA Tool started at http://localhost:8001")
    print(f"👉 In VIA: Click 'Add Files' and upload from:\n   {processed_dir}")

# --- Run ---
if __name__ == "__main__":
    print("🔧 Preprocessing images...")
    preprocess()

    print("🧠 Annotating basic features...")
    annotate()

    print("🚀 Launching VIA Tool...")
    start_via()

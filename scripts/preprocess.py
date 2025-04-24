import cv2
import os
from skimage import exposure

def preprocess_all_images(raw_dir, processed_dir):
    os.makedirs(processed_dir, exist_ok=True)

    for f in os.listdir(raw_dir):
        if f.lower().endswith(('.jpg', '.png', '.jpeg')):  # Only process image files
            path = os.path.join(raw_dir, f)
            out = os.path.join(processed_dir, f)
            img = cv2.imread(path)

            # Resize the image
            img = cv2.resize(img, (512, 512))

            # Apply gamma correction
            img = exposure.adjust_gamma(img, 1.2)

            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Save the processed image
            cv2.imwrite(out, gray)

            print(f"Processed: {f}")

    print("✅ Preprocessing complete!")

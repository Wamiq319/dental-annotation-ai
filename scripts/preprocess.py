import os
import cv2
import pydicom
from PIL import Image
import numpy as np

def dicom_to_array(dcm_path):
    ds = pydicom.dcmread(dcm_path)
    img = ds.pixel_array
    if len(img.shape) == 2:  # Convert grayscale to RGB
        img = np.stack((img,)*3, axis=-1)
    return cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')

def process_image(input_path, output_size=(1024,1024)):
    if input_path.lower().endswith('.dcm'):
        img = dicom_to_array(input_path)
    else:
        img = cv2.imread(input_path)
    
    # Standardize orientation (common issue in dental scans)
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) if img.shape[0] > img.shape[1] else img
    
    # Enhance contrast for better annotation
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    limg = cv2.merge((clahe.apply(l), a, b))
    enhanced = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    
    return cv2.resize(enhanced, output_size)

# Batch processing
for filename in os.listdir('data/raw'):
    input_path = os.path.join('data/raw', filename)
    output_path = os.path.join('data/processed', f"{os.path.splitext(filename)[0]}.jpg")
    cv2.imwrite(output_path, process_image(input_path))
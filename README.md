# Dental Image Annotation Project

Project for annotating dental images using VGG Image Annotator (VIA) in GitHub Codespaces.

## Setup

1. Open in GitHub Codespaces
2. Install dependencies: `pip install -r requirements.txt`
3. Place raw images in `data/raw/`

## Usage

1. Preprocess images: `python scripts/preprocess.py`
2. Start VIA annotator: `python scripts/serve_via.py`
3. Access VIA at the URL shown (port 8000)
4. Annotations will be saved in `annotations/`
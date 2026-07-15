# Pattern Recognition in Python

A collection of Python scripts for image processing and pattern recognition using **OpenCV** and **scikit-learn**. The codebase demonstrates techniques like grayscale conversion, binary thresholding, pixel-level analysis, RGB extraction, coordinate tracking from mouse interactions, and K-Nearest Neighbors classification.

## Features

### Image Processing
| File | Description |
|------|-------------|
| `turnblacknwhite.py` | Converts color images to black-and-white using Otsu's thresholding method with OpenCV |
| `pattern.py` | Visualizes images and retrieves pixel coordinates via double-click interaction |
| `ejemplo.py` | Extracts RGB values from image pixels at mouse click positions in a loop |

### Pattern Recognition & Classification
| File | Description |
|------|-------------|
| `knn.py` | K-NN classifier that scores images based on binary pixel patterns (white/colored regions), uses train-test split and accuracy evaluation |
| `pixel.py` | Pixel-level analysis converting image to a sequence of '0'/'1' labels based on color values |
| `clasificador.py` *(incomplete)* | Partial implementation for parametric multivariate classification with mean estimation and covariance matrix computation |

## Requirements

```bash
pip install opencv-python numpy scikit-learn matplotlib pillow
```

## Usage Notes

All scripts require the following input files (create them first):
- `bw_image.jpg` - Black & white image for pixel analysis
- `boscosobw.jpg` - Forest/black-and-white image for KNN testing  
- `cielocolor.png` - Color sky image to demonstrate grayscale conversion and thresholding

## Workflow Example

1. **Preprocess**: Use `turnblacknwhite.py` to binarize images with Otsu's method
2. **Analyze pixels**: Extract pixel data using `pixel.py` or interactively with `ejemplo.py`/`pattern.py`  
3. **Classify patterns**: Apply KNN classifier from `knn.py` to predict image regions

## Note

The repository contains experimental/completed scripts and one incomplete implementation (`clasificador.py`)
# Face Detection with OpenCV in Colab

This project demonstrates a simple face detection application using OpenCV in Google Colab. It captures a photo using the webcam, processes it to detect faces using a Haar Cascade classifier, and displays the result with bounding boxes around detected faces.

## Prerequisites

- Google Colab environment
- Webcam access enabled in the browser
- Basic Python knowledge

## Installation

The required libraries are installed directly in the Colab notebook:

```bash
!pip install opencv-python-headless
```

## Usage

1. **Run the Notebook**:
   - Open the notebook in Google Colab.
   - Execute the cells in sequence to:
     - Install OpenCV.
     - Import necessary libraries.
     - Define a function to capture a photo via the webcam.
     - Load and process the image for face detection.
     - Display the output with detected faces.

2. **Capturing a Photo**:
   - The `take_photo` function creates a browser-based interface with a "Capture Photo" button.
   - Click the button to take a photo using your webcam.

3. **Face Detection**:
   - The script uses OpenCV's Haar Cascade classifier (`haarcascade_frontalface_default.xml`) to detect faces.
   - Adjustable parameters (`scaleFactor`, `minNeighbors`, `minSize`) control detection sensitivity.
   - Detected faces are outlined with green rectangles.

4. **Output**:
   - The number of detected faces is printed.
   - The processed image with bounding boxes is displayed using PIL.

## Code Overview

- **Libraries**: Uses `opencv-python-headless`, `numpy`, `PIL`, and JavaScript for webcam access.
- **Photo Capture**: JavaScript code in Colab captures a webcam image and saves it as a JPEG.
- **Face Detection**: OpenCV processes the image in grayscale and applies the Haar Cascade classifier.
- **Visualization**: Converts the image to RGB and displays it with bounding boxes.

## Notes

- Ensure your browser allows webcam access for Colab.
- Adjust `scaleFactor`, `minNeighbors`, and `minSize` in the `detectMultiScale` function to improve detection accuracy based on your needs.
- The Haar Cascade classifier may not detect faces in all lighting conditions or angles; consider experimenting with parameters or using deep learning-based models for better performance.

## License

This project is licensed under the MIT License.
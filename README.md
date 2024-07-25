# Pencil Sketch Generator

Pencil Sketch Generator is a simple Tkinter-based Python application that converts an image into a pencil sketch. This application uses OpenCV for image processing.

## Features

- Load an image from your file system.
- Convert the loaded image to a pencil sketch.
- Preview the pencil sketch in a new window.
- Save the pencil sketch to your file system.

## Requirements

- Python 3.x
- Tkinter
- OpenCV
- PIL (Pillow)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/pencil-sketch-generator.git
    cd pencil-sketch-generator
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python pencil_sketch_generator.py
    ```

## Usage

1. Click the **Open Image** button to load an image from your file system.
2. The application will convert the image to a pencil sketch and display it in a new window.
3. If you want to save the pencil sketch, click the **Save Image** button and choose the location where you want to save the file.

## Code Explanation

- `pencil_sketch(image_path)`: This function takes the path of an image and converts it into a pencil sketch using OpenCV functions.
- `open_file()`: This function opens a file dialog to choose an image file, generates the pencil sketch, and displays it in a new window.
- `display_image(img_array)`: This function displays the generated pencil sketch in a new Tkinter window.
- `save_file()`: This function saves the generated pencil sketch to a specified location.


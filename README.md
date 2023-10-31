# License Plate Detection Project

This project is designed to perform license plate detection on images. It provides functionalities to allow users to select an image, identify and draw a box around the license plate in the image, extract the text from the detected license plate, and display it both on the image and in the console.

## Features

- **File Selection:** The program enables the user to select an image file.
- **Image Processing:** It opens the selected image and uses image processing techniques to detect the license plate.
- **License Plate Detection:** It draws a bounding box around the detected license plate in the image.
- **Text Extraction:** The program reads the text from the detected license plate.
- **Display:** It writes the extracted text on top of the bounding box in the image and also displays the text in the console.

## Usage

1. **Select Image:** Run the program and use the file selector to choose the image containing the license plate.
2. **View Results:** The program will display the image with a bounding box around the detected license plate and print the extracted text in the console.

## Installation and Setup

To use this project, follow these steps:

1. Clone this repository: `git clone https://github.com/MayiVT/License-plate-detector`
2. Install the necessary dependencies: `pip install -r requirements.txt`
3. Run the program: `python main.py`

Make sure to have Python installed on your system.

## Dependencies

The project relies on the following main libraries:
- OpenCV: For image processing and object detection.
- Tesseract OCR: For extracting text from the detected license plate.

## Contributions

Contributions to improve and expand this project are welcome! Feel free to open issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

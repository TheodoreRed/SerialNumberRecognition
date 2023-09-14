# Serial Number Recognition with Raspberry Pi and Tesseract OCR

Utilize the power of the Raspberry Pi, coupled with the Pi Camera and Tesseract OCR, to capture images of bills and recognize serial numbers. The script then cross-references these serial numbers with a predefined list of special serial numbers and provides additional checks for their properties.

## Prerequisites

- **Raspberry Pi** with Raspbian installed.
- **Raspberry Pi Camera** module connected.

## Dependencies

Install the following libraries and packages:

- OpenCV (`cv2`)
- Tesseract (`pytesseract`)
- Raspberry Pi Camera Python library (`picamera`)
- NumPy (`numpy`)

### Installation Steps

1. **Set up your Raspberry Pi Camera**: 
Follow the [official guide](https://www.raspberrypi.org/documentation/configuration/camera.md) to connect and enable the camera.

2. **Install the required dependencies**:
   ```bash
   sudo apt-get update
   sudo apt-get install tesseract-ocr libtesseract-dev libleptonica-dev pkg-config
   pip3 install opencv-python pytesseract picamera numpy


## Setup & Execution

1. **Clone the repository**:
    ```bash
    git clone <repo-url>
    cd <repo-directory>
    ```

2. **Generate Special Serial Numbers**:
    ```
    python3 generate_serials.py
    ```
    This will populate the `special_serials.txt` file.

3. **Run the main script**:
    ```bash
    python3 scanner.py
    ```

## Results

Once the script is executed, check the printed output on the terminal for the results of the recognition and the checks.

## Function Descriptions

- **`capture_image()`**: Captures an image using the Raspberry Pi camera.
- **`preprocess_image(image)`**: Preprocesses the image to improve OCR results.
- **`recognize_serial(roi_image)`**: Recognizes the serial number from the image's region of interest (ROI).
- **`is_special_serial(serial, special_serials_set)`**: Checks if the serial is in the list of special serial numbers.
- **`is_solid_binary_trinary(num)`**: Checks if a number is solid, binary, or trinary.

## Support

For assistance or inquiries, open an issue or contact the project's maintainer.

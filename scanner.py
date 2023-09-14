import cv2
import pytesseract
import picamera
from picamera.array import PiRGBArray
import numpy as np
import time


def capture_image():
    """Capture an image using the Raspberry Pi camera and return it as a NumPy array."""
    with picamera.PiCamera() as camera:
        time.sleep(3)
        rawCapture = PiRGBArray(camera)
        camera.capture(rawCapture, format="bgr")
        image = rawCapture.array
    return image


def preprocess_image(image):
    """Preprocess the image for better OCR results."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )
    denoised = cv2.fastNlMeansDenoising(thresh, None, 30, 7, 21)
    resized = cv2.resize(denoised, (2 * denoised.shape[1], 2 * denoised.shape[0]))

    # Extract region of interest (ROI). Adjust the coordinates based on your setup.
    x_start, y_start, x_end, y_end = 100, 100, 300, 300
    roi = resized[y_start:y_end, x_start:x_end]

    return roi


def recognize_serial(roi_image):
    """Recognize the serial number using Tesseract OCR."""
    temp = pytesseract.image_to_string(roi_image, config="--psm 6").strip()
    return temp[1 : len(temp) - 1]


def is_special_serial(serial, special_serials_set):
    """Check if the recognized serial number is in the list of special serial numbers."""
    return serial in special_serials_set


def is_solid_binary_trinary(num):
    """Check if the serial number contains exactly one, two, or three unique characters."""
    unique_nums = len(set(num))
    return unique_nums == 1 or unique_nums == 2 or unique_nums == 3


def is_palindrome(num):
    pass


if __name__ == "__main__":
    # 1. Capture the image
    image = capture_image()
    cv2.imshow("Captured Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 2. Preprocess the image
    roi = preprocess_image(image)

    # 3. Use Tesseract to recognize the serial number
    serial_number = recognize_serial(roi)

    # Set of special serial numbers
    special_serials = set()
    with open("special_serials.txt", "r") as file:
        for number in file:
            special_serials.add(number.strip())

    # 4. Check if the serial number is special
    if is_special_serial(serial_number, special_serials):
        # Do something
        print(True)

    # 5. Check if the serial number is solid, binary, or trinary
    if is_solid_binary_trinary(serial_number):
        # Do something
        print(True)

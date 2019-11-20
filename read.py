import cv2
import time
import os
from PIL import Image
from pytesseract import image_to_string


def read_image():
    # Log the time
    time_start = time.time()

    # Object to capture results
    text_from_image = {}

    # Try to read the image
    try:
        print('Reading image ...\n')
        text_from_image = image_to_string(Image.open(
            "./dump-ticket.jpeg"), lang='eng', config='', nice=0, output_type='dict')
    except Exception as e:
        print(e)

    print("It took %d seconds for conversion. \n" % (time.time() - time_start))
    return text_from_image


def test_reader():
    result = read_image()
    assert bool(result) == True, "Could not read anything from the image"
    print("All tests passed! \n")
    print(result)


if __name__ == "__main__":
    test_reader()

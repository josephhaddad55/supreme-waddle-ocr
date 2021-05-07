import time

from PIL import Image
from pytesseract import image_to_string


def read_image():
    # Log the time
    time_start = time.time()

    # Object to capture results
    text_from_image = {}

    # Try to read the image
    try:
        print("Reading image ...\n")
        text_from_image = image_to_string(
            Image.open("./dump-ticket.jpeg"),
            lang="eng",
            config="",
            nice=0,
            output_type="dict",
        )
    except Exception as e:
        print(e)

    print(f"It took {time.time() - time_start} seconds for conversion. \n")
    return text_from_image


if __name__ == "__main__":
    print(read_image())

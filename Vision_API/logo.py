import sys
import io
from google.cloud import vision


def detect_logos_uri(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    print("Logos:")

    for logo in logos:
        print(logo.description)

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(
                response.error.message)
        )


if __name__ == '__main__':
    detect_logos_uri(sys.argv[1])

# python logo.py https://media.designrush.com/inspirations/129839/conversions/_1611238414_61_lego-logo-1-preview.jpg

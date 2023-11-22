import sys
import io
from google.cloud import vision


def detect_text_uri(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    print(texts[0].description)

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(
                response.error.message)
        )


if __name__ == '__main__':
    detect_text_uri(sys.argv[1])

# python text.py https://www.eastcoast-nsa.gov.tw/image/6921/1024x768

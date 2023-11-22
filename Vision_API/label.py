import sys
import io
from google.cloud import vision


def detect_labels_uri(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print("Labels:")

    for label in labels:
        print(label.description)

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(
                response.error.message)
        )


if __name__ == '__main__':
    detect_labels_uri(sys.argv[1])

# python label.py https://obs.line-scdn.net/0haMeSq0mrPmJYKiwwBcFBNWB8MhNrTCRrehglUyl5NVsgBno8ZEltAXp6Zk4mG3AxeB8iA3R_YlB0Gno1Zg/w644
# python label.py https://www.eastcoast-nsa.gov.tw/image/6921/1024x768

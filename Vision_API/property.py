import sys
import io
from google.cloud import vision


def detect_properties_uri(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    print("Properties:")

    for color in props.dominant_colors.colors:
        print(f"frac: {color.pixel_fraction}")
        print(f"\tr: {color.color.red}")
        print(f"\tg: {color.color.green}")
        print(f"\tb: {color.color.blue}")
        print(f"\ta: {color.color.alpha}")

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(
                response.error.message)
        )


if __name__ == '__main__':
    detect_properties_uri(sys.argv[1])

# python property.py https://media.designrush.com/inspirations/129839/conversions/_1611238414_61_lego-logo-1-preview.jpg

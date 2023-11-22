import sys
import io
from google.cloud import vision


def detect_web_uri(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.web_detection(image=image)
    annotations = response.web_detection

    if annotations.best_guess_labels:
        for label in annotations.best_guess_labels:
            print(f"\nBest guess label: {label.label}")

    if annotations.pages_with_matching_images:
        print(
            "\n{} Pages with matching images found:".format(
                len(annotations.pages_with_matching_images)
            )
        )

        for page in annotations.pages_with_matching_images:
            print(f"\n\tPage url   : {page.url}")

            if page.full_matching_images:
                print(
                    "\t{} Full Matches found: ".format(
                        len(page.full_matching_images))
                )

                for image in page.full_matching_images:
                    print(f"\t\tImage url  : {image.url}")

            if page.partial_matching_images:
                print(
                    "\t{} Partial Matches found: ".format(
                        len(page.partial_matching_images)
                    )
                )

                for image in page.partial_matching_images:
                    print(f"\t\tImage url  : {image.url}")

    if annotations.web_entities:
        print("\n{} Web entities found: ".format(
            len(annotations.web_entities)))

        for entity in annotations.web_entities:
            print(f"\n\tScore      : {entity.score}")
            print(f"\tDescription: {entity.description}")

    if annotations.visually_similar_images:
        print(
            "\n{} visually similar images found:\n".format(
                len(annotations.visually_similar_images)
            )
        )

        for image in annotations.visually_similar_images:
            print(f"\tImage url    : {image.url}")

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(
                response.error.message)
        )


if __name__ == '__main__':
    detect_web_uri(sys.argv[1])

# python web.py https://obs.line-scdn.net/0haMeSq0mrPmJYKiwwBcFBNWB8MhNrTCRrehglUyl5NVsgBno8ZEltAXp6Zk4mG3AxeB8iA3R_YlB0Gno1Zg/w644

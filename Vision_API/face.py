import sys
import io
from google.cloud import vision


def detect_faces_uri(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = (
        "UNKNOWN",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    )
    print("Faces:")

    count = 1

    for face in faces:
        print(f"Face{count}")
        print(f"joy: {likelihood_name[face.joy_likelihood]}")
        print(f"sorrow: {likelihood_name[face.sorrow_likelihood]}")
        print(f"anger: {likelihood_name[face.anger_likelihood]}")
        print(f"surprise: {likelihood_name[face.surprise_likelihood]}")

        vertices = [
            f"({vertex.x},{vertex.y})" for vertex in face.bounding_poly.vertices
        ]

        print("face bounds: {}".format(",".join(vertices)))
        print()
        count += 1

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(
                response.error.message)
        )


if __name__ == '__main__':
    detect_faces_uri(sys.argv[1])

# python face.py https://obs.line-scdn.net/0haMeSq0mrPmJYKiwwBcFBNWB8MhNrTCRrehglUyl5NVsgBno8ZEltAXp6Zk4mG3AxeB8iA3R_YlB0Gno1Zg/w644

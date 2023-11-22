import sys
import io
from google.cloud import vision


def detect_landmarks_uri(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations
    print("Landmarks:")

    for landmark in landmarks:
        print(landmark.description)

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(
                response.error.message)
        )


if __name__ == '__main__':
    detect_landmarks_uri(sys.argv[1])

# python landmark.py https://api.housefeel.com.tw/wp-content/uploads/2021/10/230804%E5%8F%B0%E5%8C%97101-%E7%82%BA%E4%BB%80%E9%BA%BC%E5%8F%AF%E4%BB%A5%E8%93%8B%E9%80%99%E9%BA%BC%E9%AB%98%EF%BC%9F%E7%82%BA%E4%BB%80%E9%BA%BC%E5%B8%82%E4%B8%AD%E5%BF%83%E6%9C%89%E6%91%A9%E5%A4%A9%E5%A4%A7%E6%A8%93%EF%BC%9F%E5%8F%B0%E5%8C%97101%E8%88%88%E5%BB%BA%E6%95%85%E4%BA%8B%EF%BC%81og.png
# python landmark.py https://ak-d.tripcdn.com/images/010292224rd4zyqv5E9D1_W_800_0_R5_Q90.jpg

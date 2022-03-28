import urllib
from urllib.request import urlopen
import face_recognition
from PIL import Image

def getface(url):
    faceImg = urlopen(url)
    image = face_recognition.load_image_file(faceImg)
    face_locations = face_recognition.face_locations(image)

    face_location = face_locations[0]
    top, right, bottom, left = face_location
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    return pil_image.show()

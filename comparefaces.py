import urllib
import face_recognition


def getConfidence(dist):
    if dist >= 0.5:
        distanceValue = dist - 0.5
    else:
        distanceValue = 0.5 - dist
    confidence = distanceValue * 100 / 0.5
    return confidence


def comparefaces(faceFromId, faceFromCamera):
    try:
        faceImgFromId = urllib.request.urlopen(faceFromId)
        faceImgFromCamera = urllib.request.urlopen(faceFromCamera)
        imageFromId = face_recognition.load_image_file(faceImgFromId)
        imageFromCamera = face_recognition.load_image_file(faceImgFromCamera)

        faceEncodingFromId = face_recognition.face_encodings(imageFromId)
        faceEncodingFromCamera = face_recognition.face_encodings(imageFromCamera)

        isMatching = False

        if len(faceEncodingFromId) > 0 and len(faceEncodingFromCamera) > 0:
            facesFound = True
            match_results = face_recognition.compare_faces([faceEncodingFromCamera[0]], faceEncodingFromId[0])
            distance = face_recognition.face_distance([faceEncodingFromCamera[0]], faceEncodingFromId[0])

            conf = getConfidence(distance[0])
            # print("distance", distance)
            # print("confidence", conf)

            if match_results[0]:
                isMatching = True
            else:
                isMatching = False
        else:
            facesFound = False

        return {
            "facesFound": facesFound,
            "isMatching": isMatching,
            "faceDistance": distance[0],
            "confidence": conf
        }
    except Exception as e:
        print("error", e)
        return {
            "error": e,
        }

# print(comparefaces("https://i.ibb.co/vYt0tLx/sudaraka.jpg", "https://i.ibb.co/fSjw45x/sudaraka.jpg"))

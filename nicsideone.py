import io
import cv2
import requests
import datefinder
import numpy as np
import pytesseract
from PIL import Image
from urllib.request import urlopen


def url_to_image(url, readFlag=cv2.IMREAD_COLOR):
    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, readFlag)
    return image


def setdatasideone(input):
    try:
        img = url_to_image(input)
        img = cv2.resize(img, None, fx=2, fy=2)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        data = {
            "nic": "",
            "dateOfBirth": "",
            "gender": "",
            "name": "",
            "confidence": 0,
        }
        isValidNic = False
        isSL = False

        config_init = '--oem 3 --psm %d' % 1
        outputToConf = pytesseract.image_to_data(img, config=config_init, lang='eng', output_type='data.frame')

        text = outputToConf[outputToConf.conf != -1]

        conf = text.groupby(['block_num'])['conf'].mean()

        confValue = 0
        for s in conf:
            confValue = confValue + s

        for psm in range(12, 12 + 1):
            config = '--oem 3 --psm %d' % psm
            output = pytesseract.image_to_string(img, config=config, lang='eng')
            outputCapitalized = output.capitalize()
            outputArray = output.split("\n")

            for i in outputArray:
                if "Name" in i:
                    if ":" in i:
                        data["name"] = i.split(":")[1]
                    else:
                        data["name"] = i

                if len(i) == 12 and i.isnumeric():
                    data["nic"] = i

                dateMatches = list(datefinder.find_dates(i))
                if len(dateMatches) > 0:
                    dob = dateMatches[0]
                    dobDate = dob.strftime("%d")
                    dobMonth = dob.strftime("%m")
                    dobYear = dob.strftime("%Y")
                    data["dateOfBirth"] = dobDate+"/"+dobMonth+"/"+dobYear

                if "Male" in i:
                    data["gender"] = "Male"
                elif "Female" in i:
                    data["gender"] = "Female"

                if "NATIONAL IDENTITY CARD" in i:
                    isValidNic = True
                if "SRI LANKA" in i or "SRILANKA" in i:
                    isSL = True

        responseForName = requests.get(input)
        imgForName = Image.open(io.BytesIO(responseForName.content))
        outputForName = pytesseract.image_to_string(imgForName)
        outputArrayForName = outputForName.split("\n")

        for i in outputArrayForName:
            if "Name:" in i:
                if ":" in i:
                    name = i.split(":")[1]
                    data["name"] = name

        data["confidence"] = confValue/len(conf)

        if not isValidNic:
            return "Not a valid NIC"
        elif not isSL:
            return "Not a valid Sri Lankan NIC"
        elif data["nic"] == "" or data["dateOfBirth"] == "" or data["gender"] == "" or data["name"] == "":
            return "The uploaded image is not quality enough to extract data"
        return data
    except Exception as e:
        return {
            "error": e
        }

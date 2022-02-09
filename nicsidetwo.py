import cv2
import numpy as np
import pytesseract
from urllib.request import urlopen

def url_to_image(url, readFlag=cv2.IMREAD_COLOR):
    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, readFlag)
    return image

def setdatasidetwo(input):
    try:
        img = url_to_image(input)
        img = cv2.resize(img, None, fx=2, fy=2)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        data = {
            "address": "",
            "confidence": 0,
        }

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
            subDataArray = []

            for i in outputArray:
                if "," in i:
                    subDataArray.append(i)

            for d in subDataArray:
                if d.isupper() == True:
                    data["address"] = d

        data["confidence"] = confValue/len(conf)

        if data["address"] == "":
            return "The uploaded image is not quality enough to extract data"
        return data
    except Exception as e:
        return {
            "error": e
        }

import urllib
import pytesseract
import io
import requests
from PIL import Image
from getLicenceNumber import getLicenceNumber
from getNic import getNic
from getName import getName
from getAddress import getAddress
from getBloodGroup import getBloodGroup
import cv2
import numpy as np

from urllib.request import urlopen


def url_to_image(url, readFlag=cv2.IMREAD_COLOR):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, readFlag)

    # return the image
    return image


def textProcess(text):
    fullTextArray = []
    linesArray = text.split("\n")
    for line in linesArray:
        rowStrings = line.split(" ")
        for text in rowStrings:
            if text != "":
                fullTextArray.append(text)
    finalString = " ".join(fullTextArray)
    capitalizedString = finalString.title()
    return capitalizedString


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def setLicense(input):
    try:
        img = url_to_image(input)

        #  img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
        img = cv2.resize(img, None, fx=2, fy=2)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        data = {
            "licenceNo": "",
            "nic": "",
            "dateOfBirth": "",
            "gender": "",
            "name": "",
            "address": "",
            "bloodGroup": "",
            "confidence": 0,
        }
        isValidLicence = False
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

            if data["licenceNo"] == "":
                data["licenceNo"] = getLicenceNumber(outputArray)["licenceNo"]

            namesString = ""
            addressString = ""

            print("output array", outputArray)

            for i in outputArray:
                if data["nic"] == "":
                    data["nic"] = getNic(i, outputArray)["nic"]

                if data["dateOfBirth"] == "":
                    data["dateOfBirth"] = getNic(i, outputArray)["dob"]

                if data["gender"] == "":
                    data["gender"] = getNic(i, outputArray)["gender"]

                if data["bloodGroup"] == "" or data["bloodGroup"] == "Not detected":
                    data["bloodGroup"] = getBloodGroup(i)

                if "DRIVING LICENCE" in i:
                    isValidLicence = True
                if "SRI LANKA" in i:
                    isSL = True

                if data["name"] == "":
                    if i.isupper() and not "LICENCE" in i and not "SRI LANKA" in i:
                        if not ((len(i) == 9 or len(i) == 8 or len(i) == 7) and hasNumbers(i)):
                            addressString = addressString + " " + i
                        if not ("8" in i or "3" in i) and len(namesString.split(" ")) < 5:
                            namesString = namesString + "\n" + i

            data["name"] = getName(textProcess(namesString.capitalize()))

        if data["address"] == "":
            responseForAddress = requests.get(input)
            imgForAddress = Image.open(io.BytesIO(responseForAddress.content))
            outputForAddress = pytesseract.image_to_string(imgForAddress)
            outputArrayForAddress = outputForAddress.split("\n")
            # print("outputArrayForAddress", outputArrayForAddress)
            addressNewString = ""

            for i in outputArrayForAddress:
                if i.isupper() and not "LICENCE" in i and not "SRI LANKA" in i:
                    if '8.' in i or '5.' in i:
                        addressNewString = i

        # data["address"] = getAddress(textProcess(addressString.capitalize()), data["name"])
        data["address"] = getAddress(textProcess(addressNewString.capitalize()))

        data["confidence"] = confValue / len(conf)

        print("data", data)

        if not isValidLicence:
            return "Not a valid Driving Licence"
        elif not isSL:
            return "Not a valid Sri Lankan Driving Licence"
        elif data["licenceNo"] == "" or data["nic"] == "" or data["dateOfBirth"] == "" or data["gender"] == "" or data[
            "name"] == "" or data["bloodGroup"] == "":
            return "The uploaded image is not quality enough to extract data"
        return data
    except Exception as e:
        return {
            "error": e
        }

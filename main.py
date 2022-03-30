import pytesseract
from flask import Flask
from flask_restful import Resource, Api, reqparse
from nicsideone import setdatasideone
from nicsidetwo import setdatasidetwo
from licensedata import setLicense
from facedata import getface
from comparefaces import comparefaces
from eyeblinking import blinkingProcess

app = Flask(__name__)
api = Api(app)
# pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'

# detectedFace = getface("https://i.ibb.co/crhmxBB/kasun1.jpg")
# print("faces", comparefaces("https://i.ibb.co/vYt0tLx/sudaraka.jpg", "https://i.ibb.co/fSjw45x/sudaraka.jpg"))

url1 = "https://psrtempbucket.s3.ap-south-1.amazonaws.com/temp_dls/blink1.webm"
url2 = "https://psrtempbucket.s3.ap-south-1.amazonaws.com/temp_dls/kausikan.webm"
url3 = "https://smart-cap.obs.ap-southeast-3.myhuaweicloud.com/1648199202430_1648199202430.webm"
# print("blinks", blinkingProcess(url3))

# niceUrl1 = "https://i.ibb.co/Lpttzzq/NIC-front.jpg"
# niceUrl2 = "https://i.ibb.co/WghtK4M/NIC-back.jpg"
drivinglicense = "https://i.ibb.co/M5XvzrY/lashan.jpg"
drivinglicense2 = "https://i.ibb.co/SQyWWSH/sudaraka.jpg"
drivinglicense3 = "https://i.ibb.co/ZXG9rnq/chopra.jpg"

drivinglicense4 = "https://i.ibb.co/qD6Qx38/isira1.jpg"
drivinglicense5 = "https://i.ibb.co/3zDL14Y/pradeepa.jpg"
drivinglicense6 = "https://i.ibb.co/MMntrq6/prasad.jpg"
drivinglicense7 = "https://i.ibb.co/DMdxPph/prasad2.jpg"
# print("nic one", setdatasideone(niceUrl1))
# print("nic two", setdatasidetwo(niceUrl2))
# print("driving", setLicense(drivinglicense2))

class idDataSideOne(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('imageUrl', required=True)
        args = parser.parse_args()  # parse arguments to dictionary
        return {'data': setdatasideone(args['imageUrl'])}, 200  # return data and 200 OK code

    pass


class idDataSideTwo(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('imageUrl', required=True)
        args = parser.parse_args()  # parse arguments to dictionary
        return {'data': setdatasidetwo(args['imageUrl'])}, 200  # return data and 200 OK code

    pass


class licenseData(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('imageUrl', required=True)
        args = parser.parse_args()  # parse arguments to dictionary
        return {'data': setLicense(args['imageUrl'])}, 200  # return data and 200 OK code

    pass


class getIdFace(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('imageUrl', required=True)
        args = parser.parse_args()  # parse arguments to dictionary
        return {'data': getface(args['imageUrl'])}, 200  # return data and 200 OK code

    pass


class getfacematching(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('facefromid', required=True)
        parser.add_argument('facefromcamera', required=True)
        args = parser.parse_args()  # parse arguments to dictionary
        return {'data': comparefaces(args['facefromid'], args['facefromcamera'])}, 200  # return data and 200 OK code

    pass


class getBlinkingCount(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('videoUrl', required=True)
        args = parser.parse_args()  # parse arguments to dictionary
        return {'data': blinkingProcess(args['videoUrl'])}, 200  # return data and 200 OK code

    pass

api.add_resource(idDataSideOne, '/nicsideone')
api.add_resource(idDataSideTwo, '/nicsidetwo')
api.add_resource(licenseData, '/license')
api.add_resource(getIdFace, '/getidface')
api.add_resource(getfacematching, '/getidfacematching')
api.add_resource(getBlinkingCount, '/islive')

if __name__ == '__main__':
    app.run()

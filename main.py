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
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'

# detectedFace = getface("https://i.ibb.co/crhmxBB/kasun1.jpg")
# print("faces", comparefaces("https://i.ibb.co/vYt0tLx/sudaraka.jpg", "https://i.ibb.co/fSjw45x/sudaraka.jpg"))

# url = "https://psrtempbucket.s3.ap-south-1.amazonaws.com/temp_dls/blink1.webm?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDmFwLXNvdXRoZWFzdC0xIkgwRgIhAO%2F3MAV1VIT1IsjINJWSW39xYGcqWsrZiq3BCmtbFFIPAiEA9N1R2NUKuPVlTJk78RrQjjefCI%2FkQOTs4yEzG42UjWwq9gIIfRAAGgwxODUzOTQ2OTM4MDQiDG0gCJbhLStbfgVGLirTAhxs8wOxx6rejaFzE80Zyfp%2FSn2YMGNuEBrbboGCRFLu6U16wWtoCvzHJ4KOK5TSqaEyutlKu4nqGwpXKJRmLxfusOxFKChcTTK8NwIdUzHbTWoW65DLwzXf2BXqVjlCFszplwX9jJC42htymSFFFwuKb8oQOG5fNOESOTNJbE51SPDsJ4gNWsejHgA%2F2mhSsV8aWsRELelY2qH7P7lFO%2B6aOoxA76y%2BY4JCFnMVaWQsC70k%2B5kQvNutifNKDWOv1n0DIoaKs9P8xK4lwcYYzWJXYvCPQJn0T4xUciqqtSJa1tvW%2FfM4cvHyO7aGkkHURYEde29A%2Bna0GvRgWHSrRs23YK8YwIK57Wqa%2BNuS1GOqmTZS5boWeU875if8CDaqlms1W5IM4cYmlmPpdXy0nIphIHyApr52STf11oOV%2B3h1x2WjPbFxywIp07I50Fbc2WAIdjC2rLSNBjqyAiENmqNoPlq6stOb%2FdfWALk%2FpueJYNi1xQe5ShcSpDf2qM%2FpSs1YRA2cBulN4uLvHKBZQj1vFtKw21RomOoOIcePRRK66%2F9E9s%2FDmPtCn%2BC9CL8UFuyBBa0CC2uFmfEWmBOZAPPLlEkpfXSnL0os3imZ43MG28FzaVTK%2BeuNisb1%2BHyyLPTPeyq8hVudpp16zstXUl84nf3qcWZ8o2kTFtTr0syVOv39FPaVypA%2F%2F%2F4vHmOftuPfi%2BxHhX5VfkKtoAfmI0xz10C2fZWSUVEnsYgpmvCeul1rYWPUcfF6Vx8gD9ERO1j30jVbbugAEkodR2eiQqq7LRVvU%2B1r%2ByMR5jztDJoHNKP%2FGuedWctcMINfa%2BNTJwhz0qLpUEuVHC2MoDeQQ9reSljb3zoXbRUygnXsZA%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20211205T204430Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIASWKTCQ2WGPH3SONV%2F20211205%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Signature=22ee1329125b98a775236a8ee9a70fc5fd598a1e9515c45aac9cce4ad5684f2c"
# print("blinks", blinkingProcess(url))

# niceUrl1 = "https://i.ibb.co/Lpttzzq/NIC-front.jpg"
# niceUrl2 = "https://i.ibb.co/WghtK4M/NIC-back.jpg"
drivinglicense = "https://i.ibb.co/M5XvzrY/lashan.jpg"
drivinglicense2 = "https://i.ibb.co/4m0gspc/sudaraka.jpg"
drivinglicense3 = "https://i.ibb.co/ZXG9rnq/chopra.jpg"

drivinglicense4 = "https://i.ibb.co/qD6Qx38/isira1.jpg"
drivinglicense5 = "https://i.ibb.co/3zDL14Y/pradeepa.jpg"
drivinglicense6 = "https://i.ibb.co/MMntrq6/prasad.jpg"
drivinglicense7 = "https://i.ibb.co/DMdxPph/prasad2.jpg"
# print("nic one", setdatasideone(niceUrl1))
# print("nic two", setdatasidetwo(niceUrl2))
# print("driving", setLicense(drivinglicense5))

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
        print("img1", args['facefromid'])
        print("img1", args['facefromcamera'])
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

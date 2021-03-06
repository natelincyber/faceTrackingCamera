import urllib
import numpy as np
import requests as r
import cv2

class IPWEBCAM(object):
    def __init__(self,root_url='192.168.2.109:8080'):
        self.url = 'http://'+root_url
        self.resolutions = {
                "0" : "1920x1080",
                "1" : "1280x720",
                "2" : "960x720",
                "3" : "720x480",
                "4" : "640x480",
                "5" : "352x288",
                "6" : "320x240",
                "7" : "256x144",
                "8" : "176x144"
                }
    def __str__(self):
        return f"remote camera @{self.url[7:]}"

    def get_image(self):
        # Get our image from the phone
        imgResp = urllib.request.urlopen(self.url + '/shot.jpg')

        # Convert our image to a numpy array so that we can work with it
        imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)

        # Convert our image again but this time to opencv format
        img = cv2.imdecode(imgNp,-1)

        return img


    def swap_camera(self, option):
        # swap the camera from thte back to the front
        # option: on - front camera / off - rear camera
        return r.get(self.url+"/settings/ffc?set={}".format(option))

    def overlay(self, option):
        # turn on of off the text overlay
        # option: on / off
        return r.get(self.url+"/settings/overlay?set={}".format(option))

    def led(self, option):
        # turn on or off the flash light
        # default: off
        if option =="on":
            return r.get(self.url+"/enabletorch")
        return r.get(self.url+"/disabletorch")

    def set_quality(self, option):
        # Set the quality of the image
        # from 0 to 100
        if option > 100:
            option = 100
        if option < 0:
            option = 0
        return r.get(self.url +"/settings/quality?set={}".format(option))

    def set_orientation(self, orientation):
        # Set the camera orientation
        # Landscape = 0
        # Portait = 1
        # Upside down = 2
        # Upside down portait = 3

        if orientation == 0:
            return r.get(self.url + "/settings/orientation?set=landscape")
        elif orientation == 1:
            return r.get(self.url + "/settings/orientation?set=portait")
        elif orientation == 2:
            return r.get(self.url + "/settings/orientation?set=upsidedown")
        elif orientation == 3:
            return r.get(self.url + "/settings/orientation?set=upsidedown_portait")

    def set_resolution(self, option):
        if option in self.resolutions:
            return r.get(self.url+"/settings/video_size?set=" + self.resolutions[option])

    def zoom(self, option):
        if option < 0:
            option = 0
        if option > 100:
            option = 100
        return r.get(self.url + "/ptz?zoom=" + str(option))

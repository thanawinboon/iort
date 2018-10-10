from twython import Twython
from passWORD import CK, CS, AT, ATS
from picamera import PiCamera
from time import sleep

twitter = Twython(CK,CS,AT,ATS)

camera = PiCamera()
camera.rotation = 0

def takePictureAfter(wait):
    sleep(wait)
    camera.capture('wow.jpg')
    camera.stop_preview()

try:
    camera.start_preview()
    takePictureAfter(3)
    
    message = "Wow, this pic iz gud"
    image = open('wow.jpg', 'rb')
    
    response = twitter.upload_media(media=image)
    media_id = [response['media_id']]
    
    twitter.update_status(status=message, media_ids=media_id)
    print("Tweeted: %s" % message)

finally:
    camera.stop_preview()
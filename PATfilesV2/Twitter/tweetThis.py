from twython import Twython
from passWORD import CK, CS, AT, ATS

twitter = Twython(CK,CS,AT,ATS)

'''
message = "https://www.youtube.com/watch?v=Vgy7QvNtxhY" + " this classical song is very lit"
image = open('imageMEEMEE.jpg', 'rb')
'''

message = "Wow"


response = twitter.upload_media(media=image)
media_id = [response['media_id']]


twitter.update_status(status=message, media_ids=media_id)
print("Tweeted: %s" % message)
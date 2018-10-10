from picamera import PiCamera
import subprocess
from time import sleep

streamcode = zf2y-r0qb-b48w-df68

try:
    camera = PiCamera(resolution=(800,600), framerate=25)

    camera.rotation = 0
    camera.annotate_text = "Pastel Geta Living Machine"

    ffmpeg = subprocess.Popen([
    'ffmpeg',
    '-re',
    '-ar', '44100',
    '-ac', '2',
    '-acodec', 'pcm_s16le',
    '-f','s16le',
    '-ac','2',
    '-i','/dev/zero',
    '-f','h264',
    '-i','-',
    '-vcodec', 'copy',
    '-acodec','aac',
    '-ab','128k',
    '-g','50',
    '-strict','experimental',
    '-f','flv',
    'rtmp://a.rtmp.youtube.com/live2/' + streamcode],stdin=subprocess.PIPE)

    camera.start_recording(ffmpeg.stdin, format='h264', quality=30, bitrate=2000000)
    camera.wait_recording(600)
finally:
    pkill = subprocess.Popen(['pkill', 'ffmpeg'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)



print("done")
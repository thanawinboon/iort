from picamera import PiCamera, Color

camera = PiCamera()

camera.start_recording('thisisforstop.h264')
camera.stop_recording()
camera.start_preview()
camera.stop_preview()
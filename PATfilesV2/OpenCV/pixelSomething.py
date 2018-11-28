import cv2
import numpy as npimport

img = cv2.imread('kirby.jpg')
px= 0
blue = 0
def howTo():
    global px, blue
    # img[100,100] is the color of the picture "img" in the pixel at coordinate of (100,100)
    px = img[100,100]
    
    # this stores the value of the B(lue) from BGR, since 0 = first position, 1 = second position and so on 
    blue = img[100,100,0]
    
    #set the color of pixel at coordinate (100,100) to become black (0,0,0)
    img[100,100] = [0,0,0]
    
    #set the color of an area of [y start:y end, x start:x end] into color [0,0,0]
    img[100:150, 100:150] = [0,0,0]

try:
    """
    cv2.imshow("Original", img)
    cv2.waitKey(0)
    """
    
    """
    img[100:150, 100:150] = [0,0,0]
    cv2.imshow("New", img)
    cv2.waitKey(0)
    """
    
    partOfPic = img[470:600, 350:500]
    img[0:130,0:150] = partOfPic
    cv2.imshow("Part duplicates", img)
    cv2.waitKey(0)
    

finally:
    cv2.destroyAllWindows()
# from PIL import Image
# import pytesseract
import cv2
# import tesseract
import numpy as np
im = cv2.imread('example_01.png', 1)
# text = pytesseract.image_to_string(Image.open('example_01.png'), lang='en')
# print(pytesseract.image_to_string(Image.open('example_01.png'), lang='en'))

cv2.namedWindow("Input Image")
cv2.imshow("Input Image", im)
cv2.waitKey(0)
cv2.destroyAllWindows()

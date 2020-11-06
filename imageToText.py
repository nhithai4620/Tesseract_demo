from PIL import Image
import pytesseract
# import cv2
# import os


im = Image.open("image19.png")
text = pytesseract.image_to_string(im, lang="vie")
print(text)
# image = cv2.imread("image19.png")
# gr = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# gr = cv2.threshold( gr,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU )[1]
# file = "{}.png".format(os.getpid())
# cv2.imwrite(file, gr)

# text = pytesseract.image_to_string(Image.open(file), lang="vie")
# os.remove(file)
# print(text)

import cv2 as cv

image = cv.imread("foto.png")
print(image.shape)
image2 = cv.imread("foto.png")
bw = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
gaussian_BW = cv.GaussianBlur(bw,(5,5), 0)
brightness_GBW = cv.convertScaleAbs(gaussian_BW, alpha= 10.0, beta= 10.0)

#Cropping Image
x_start = 25
x_end = 445
#-----------
y_start = 355
y_end = 776

#Input Text
font = cv.FONT_HERSHEY_SIMPLEX
fontSize = 0.8
color = (0,0,0)
thickness = 5


cropping_image  = image[x_start:x_end, y_start:y_end]
image2 = cv.putText(image2, "Annabella Wenny Sulisthio", (350,600), font, fontSize, color, thickness, cv.LINE_AA)
fileBaru1 = "Cropped.jpg"
fileBaru2 = "Text.jpg"
fileBaru3 = "Black-and-White.jpg"
fileBaru4 = "Gaussian Blur + BW.jpg"
fileBaru5 = "Brightness + BGW.jpg"

cv.imshow("Foto", image)
cv.imshow("Cropped", cropping_image)
cv.imshow("Text", image2)
cv.imshow("Black-and-White", bw)
cv.imshow("Gaussian Blur + BW", gaussian_BW)
cv.imshow("Brightness + Gaussian + BW", brightness_GBW)
cv.imwrite(fileBaru1, cropping_image)
cv.imwrite(fileBaru2, image2)
cv.imwrite(fileBaru3, bw)
cv.imwrite(fileBaru4, gaussian_BW)
cv.imwrite(fileBaru5, brightness_GBW)

cv.waitKey(0)
cv.destroyAllWindows()
import cv2

def ConvertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


img = cv2.imread("data\peeps.jpg")
resized_img = cv2.resize(img, (920, 480))
gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

img_copy = gray_img.copy()

classifier = cv2.CascadeClassifier('data\haarcascade_frontalface_alt.xml')

faces = classifier.detectMultiScale(img_copy, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in faces:
    cv2.rectangle(resized_img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv2.imshow('image', resized_img)

print(faces)

#cv2.imshow('image', resized_img)

#cv2.

cv2.waitKey(0)

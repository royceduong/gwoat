from django.shortcuts import render, redirect
from django.http import HttpResponse
import cv2
import os

def draw_on_faces(filepath): #path to image

    file = os.path.basename(filepath)
    file = os.path.splitext(file)[0]
    print (file)
    img = cv2.imread(filepath)
    resized_img = cv2.resize(img, (920, 480))
    gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

    img_copy = gray_img.copy()

    classifier = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')

    faces = classifier.detectMultiScale(img_copy, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(resized_img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

    new_file = "new_" + file + '.jpeg'
    cv2.imwrite(new_file, resized_img)
    #cv2.imwrite('blabla.jpeg', resized_img)

    cv2.waitKey(0)

    return new_file

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'first_app/home.html')

def test(request):
    return HttpResponse("Test Page")

from django.shortcuts import render, redirect
from django.http import HttpResponse
import cv2
import os
from django.core.files.storage import FileSystemStorage

def draw_on_faces(filepath): #path to image

    file = os.path.basename(filepath)
    file = os.path.splitext(file)[0]
    print (file)
    print (filepath)
    img = cv2.imread(filepath)
    #cv2.imshow('image', img)
    #cv2.waitKey(0)
    resized_img = cv2.resize(img, (920, 480))
    gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

    img_copy = gray_img.copy()

    classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    print(os.getcwd())
    faces = classifier.detectMultiScale(img_copy, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(resized_img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

    new_file =  "media/new_" + file + '.jpeg'
    cv2.imwrite(new_file, resized_img)

    cwd = os.getcwd()

    filepath = cwd + "\\" + new_file
    #cv2.imwrite('blabla.jpeg', resized_img)

    #cv2.waitKey(0)

    return filepath

def index(request):

    if request.method == 'POST':

        file = request.FILES['pic']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)

        file_url = fs.path(filename)

        new_file = draw_on_faces(file_url)

        print("File Received")
        print (new_file)
        return render(request, 'first_app/result.html', {'drawn_on_file': new_file})

    return render(request, 'first_app/home.html')

def test(request):
    return HttpResponse("Test Page")

def goats(request):
    return render(request, 'first_app/goats.html')

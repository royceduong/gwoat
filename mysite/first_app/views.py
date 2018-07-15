from django.shortcuts import render, redirect
from django.http import HttpResponse
import cv2
import os
from django.core.files.storage import FileSystemStorage
from django.contrib.staticfiles.templatetags.staticfiles import static
import random


def draw_on_faces(filepath): #path to image

    file = os.path.basename(filepath)
    file = os.path.splitext(file)[0]
    img = cv2.imread(filepath)

    resized_img = cv2.resize(img, (920, 480))
    gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

    img_copy = gray_img.copy()

    classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    print(os.getcwd())
    faces = classifier.detectMultiScale(img_copy, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        w_scaled = int(w * 1.5)
        h_scaled = int(h * 1.5)
        num =  random.randint(1, 7)
        goat_img = cv2.imread("media/goats/" + str(num) + '.jpg')
        #cv2.rectangle(resized_img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
        resized_goat = cv2.resize(goat_img, (w_scaled,h_scaled))
        for a in range(0, 920): #row
            for b in range(0, 480): #column
                if (a > x and a < x+w_scaled and (b > y and b < y + h_scaled)):
                    goat_a = x - a
                    goat_b = y - b
                    if (resized_goat[goat_b, goat_a][0] != 0 and resized_goat[goat_b, goat_a][1] != 0 and resized_goat[goat_b, goat_a][2] != 0):
                        resized_img[b,a] = resized_goat[goat_b, goat_a]


    new_file =  "new_" + file + '.jpg'
    cv2.imwrite("media/" + new_file, resized_img)

    return new_file

def index(request):

    if request.method == 'POST':

        file = request.FILES['pic']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)

        file_url = fs.path(filename)

        new_file = draw_on_faces(file_url)
        return render(request, 'first_app/result.html', {'drawn_on_file': new_file})

    return render(request, 'first_app/home.html')

def test(request):
    return HttpResponse("Test Page")

def goats(request):
    context = {
        'photos' : 12,
        'stuff' : [1,2,3,4,5,6,7,8,9,10,11,12]
    }
    return render(request, 'first_app/goats.html', context)

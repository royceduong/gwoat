from django.shortcuts import render, redirect
from django.http import HttpResponse
import cv2
import os
from django.core.files.storage import FileSystemStorage
from django.contrib.staticfiles.templatetags.staticfiles import static


def draw_on_faces(filepath): #path to image

    file = os.path.basename(filepath)
    file = os.path.splitext(file)[0]
    img = cv2.imread(filepath)

    goat_img_path = "media/goats/1.jpg"
    goat_img = cv2.imread(goat_img_path)



    resized_img = cv2.resize(img, (920, 480))
    gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

    img_copy = gray_img.copy()

    classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    print(os.getcwd())
    faces = classifier.detectMultiScale(img_copy, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        #cv2.rectangle(resized_img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
        resized_goat = cv2.resize(goat_img, (w,h))
        for a in range(0, 920): #row
            for b in range(0, 480): #column
                if (a > x and a < x+w and (b > y and b < y + h)):
                    goat_a = x - a
                    goat_b = y - b
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
        'stuff' : [1,2,3,4,5]
    }
    return render(request, 'first_app/goats.html', context)

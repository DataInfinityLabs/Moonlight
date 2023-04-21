from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.http import HttpResponse
from PIL import Image
import os
from django.conf import settings
from django.shortcuts import render
import cv2
import numpy as np
import base64

from mcore.moonlight import MoonLight
model = MoonLight()



def index(request):
    return render(request, "core/index.html")


def glowit(request):
    if request.method == 'POST':
        file = request.FILES.get('ImgFile')
        if not file:
            return HttpResponse("error!")

        image = Image.open(file)
        image_np = np.array(image)
        # convert image to cv2 format
        
        frame, number_plates = model.detect(image_np)
        print("frame",frame)


# Convert the image to a base64-encoded string

        image_basestr = "data:image/jpeg;base64," + base64.b64encode(cv2.imencode('.jpg', frame)[1]).decode('utf-8')


        
        
        context = {
            "image_basestr": image_basestr,
            "number_plates": number_plates
        }

        return render(request, "core/result.html", context)


     

     
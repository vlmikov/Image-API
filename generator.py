import base64
from itertools import count
import json
from operator import ne                    
import os
from xml.etree.ElementInclude import include
import requests
import zipfile
import math


import time
from tqdm import tqdm


validate_type = ['jpg', 'png', 'tiff' , 'jpeg' ]
def generate_batch(file_path, n):
    
    current_batch = []
    for file in os.listdir(file_path):
        curr_file_path = f"{file_path}/{file}"
        #print(curr_file_path)
        extention_file = curr_file_path.split('.')[-1]
        # extention_file = 'asa'
        print(extention_file)
        if extention_file not in validate_type:
            print('invalid')
            # invalid_files.append(curr_file_path)
            continue
        with open(curr_file_path, "rb") as image:
            f = image.read()
        current_batch.append(f)
        if len(current_batch) == n:
           yield current_batch
           current_batch = []

    if current_batch:
        yield current_batch


api = 'http://localhost:8080/files'


zip_path = "./images_zip_input"
images_from_zip = './images_form_zip/images-set'

try:
    os.mkdir(images_from_zip)
except:
    pass



        


for file in os.listdir(zip_path):
    if file.endswith('.zip'):
        number_of_files = len(os.listdir(images_from_zip))
        batch_size = 2

        batch_imgs = generate_batch(images_from_zip, n = batch_size)  
        
        number_iterate = math.floor(number_of_files/batch_size)
        counter = 0
        for batch_num in range(number_iterate-1):
            try:
                curr_batch = next(batch_imgs) 
                counter+=batch_size
            except:
                pass
        print(counter)
       
    else:
        print("грешен формат")
        continue



    
## Image API

> API for store and extract information from url image

> FASTAPI with Postgres

> Image API is create for manipulate image data from url and store information about images. 

## The first path with "GET" operation is: Home
This Home path returns simple HTML5 response.  

## The Second path with "GET" operation is : Get Images
This path with additional options: "limit" fetch data and return limit numbers of records.

## The third path with "POST" operation is : Post Image
This path accepts url of image as string. Check this url if it is image and extract following information:
- sha1 value of the file-SHA-1 : Secure Hash Algorithm 1 is a cryptographic hash function which takes an input and produces a 160-bit (20-byte) hash value
- image dimensions : Get height and width of image
- image type
- image url :  Keep all proccessed image urls 
- local url : Keep image in static folder and image urls in database

## The forth path with "DELETE" operatin is : Delete all files
Delete all records from db related to Image_info data.

## How to run?
- Clone or download this repository.
- Create virtual enviroment.
>>> python -m venv venv  
- Activate Virtual enviroment
>>> .\venv\Script\activate  (Windows)
>>> source venv/bin/activate
- Install requirements.txt
>>> pip install -r requirements.txt
- Run server
uvicorn app.main:app --reload

You can Run your image as a container too.

## In root folder of this repository there is a python file generator.py
If we put zip file with files in "./images_zip_input"
The script will extract all images in different folder, than it will iterate over the images and validate them. After that python generator will yield the image data in batches depends of our choise.
It will send the many requests to my API, but I didn't have enough time to complite this functionality. This is my first time when I use FastAPI and postgress. 



- Support server-side rendering ([example](https://github.com/docsifyjs/docsify-ssr-demo))

## Examples

If it runs go [Here]](http://127.0.0.1:8000/) to see Image API in use.


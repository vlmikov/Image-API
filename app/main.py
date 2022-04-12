import os
from fastapi import FastAPI, Depends, HTTPException, Request, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Optional
from urllib import response
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from .schema import  Images_info_full
from . import crud, models
from hashlib import sha1
from PIL import Image
import requests
from io import BytesIO
import uuid
from app.service import html


models.Base.metadata.create_all(bind=engine)



def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")






app = FastAPI()
configure_static(app)
script_dir = os.path.dirname(__file__)
st_abs_file_path = os.path.join(script_dir, "static/")
templates = Jinja2Templates(directory="templates")

def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



@app.get('/')
def home():
    content = html
    return HTMLResponse(content=content)


@app.get('/images')
async def get_images(limit: Optional[int] = 50, db=Depends(db)):
    #deleted_data = crud.delete_all_Images(db)
    #print(deleted_data)
    # print(limit)
    # return limit
    images = crud.get_all_images_info(db, limit)
    if images:
        return images
    else:
        return {"INFO": "No images!"}





async def save_image(img, file_path):
    img.save(file_path)


@app.post('/images/post_url', status_code=201)
async def post_images(url:str, db=Depends(db), request: Request=None):
    rs = requests.get(url)
    if rs.status_code == 200:
        #Check if already exist
        object_in_db = crud.get_image_info(db, url)
        if object_in_db:
            raise HTTPException(422, detail= {"INFO" : "Url already exists.",
                                                "url": url,
                                                "Object in DB for this url":{
                                                "object_id": object_in_db.id,
                                                "image_sha1" : object_in_db.image_sha1,
                                                "image_type": object_in_db.image_type,
                                                "local_url": object_in_db.local_url,
                                                "image_height":object_in_db.image_height,
                                                "image_width":object_in_db.image_width,
                                                "time_add": str(object_in_db.time_add),
                                                }
                                                })
        
        #Check if request request response is image
        try:
            img = Image.open(BytesIO(rs.content))
        except:
            return {"data":"Not image"}

        #Create unique path for image.
        file_path = f'./static/images/{uuid.uuid4()}.png'
        await save_image(img, file_path)
        #Get width and height of image.
        w,h = img.size
        #Get Secure Hash Algorithm 1 value of image
        sha_1_n = sha1(rs.content).hexdigest()
        #Get format description 
        type_img = img.format_description
        img.close()
        #set url for view image
        local_url = f"localhost:8000/{file_path}"
       
        ob_to_add = Images_info_full(image_url=url,
                                    image_sha1=sha_1_n,
                                    image_type=type_img, 
                                    local_url=local_url, 
                                    image_height=h, 
                                    image_width=w)
        await crud.save_image_info(db,ob_to_add)
        return {'INFO':'Image added successfully',
               'data':ob_to_add }
    else:
        raise HTTPException(403, detail= crud.error_message('Bad request'), headers={"X-Error": "There goes my error"})
    


@app.delete("/files")
async def delete_all_files(db=Depends(db)):
    deleted_data = crud.delete_all_Images(db)
    print(deleted_data)
    return {"INFO":"All images are removed!"}
   
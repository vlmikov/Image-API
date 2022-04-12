from requests import session
from sqlalchemy.orm import Session
from . import schema, models



def error_message(message):
    return {
        'error': message
    }

def get_all_images_info(db: Session, limit:int):
    return db.query(models.Images_info).limit(limit).all()

def get_image_info(db: Session, url: str = None):
    if url is None:
        return db.query(models.Images_info).all()
    else:
        return db.query(models.Images_info).filter(models.Images_info.image_url == url).first()

async def save_image_info(db: Session, info: schema.Images_info_full):
    image_info_model = models.Images_info(**info.dict())
    db.add(image_info_model)
    db.commit()
    db.refresh(image_info_model)
    return image_info_model


def delete_all_Images(db: Session):
    deleted = db.query(models.Images_info).delete()
    db.commit()
    return deleted
    


    
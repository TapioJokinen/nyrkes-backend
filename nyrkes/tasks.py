from celery import shared_task
from PIL import Image


@shared_task()
def resize_img(path):
    img = Image.open(path)
    if img.height > 300 or img.width > 300:
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(path)

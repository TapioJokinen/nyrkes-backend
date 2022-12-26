from celery import shared_task
from PIL import Image


@shared_task()
def resize_img(path):
    img = Image.open(path)
    if img.height > 250 or img.width > 150:
        output_size = (250, 150)
        img.thumbnail(output_size)
        img.save(path)

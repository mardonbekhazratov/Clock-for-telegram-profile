from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.account import  UpdateProfileRequest
from PIL import Image, ImageDraw, ImageFont
from random import randint
from datetime import datetime
from pytz import timezone
client = TelegramClient(session='SESSION_NAME',
                        api_id=YOUR_API_ID, api_hash="YOUR_API_HASH")
client.start()

time1 = ''
time2 = ''
date1,date2="",""

def tick():
    global time1
    global time2
    time2 = datetime.now(timezone("UTC")).astimezone(timezone("Asia/Tashkent")).strftime("%H:%M")
    if time2 != time1:
        time1 = time2
        with Image.open("Image.jpg").convert("RGBA") as base:
            img = Image.new('RGBA', base.size, (250, 250, 250, 0))
            d = ImageDraw.Draw(img)
            d.text((240,470), time2, size=1000, font=ImageFont.truetype("mexcellent3d.otf", 85), fill=(238,238,238))
            img=Image.alpha_composite(base,img)
            img.save('profile.png')
    else:
        return "NO"

def date():
    global date1
    global date2
    now=datetime.now()
    date2 = f"{now.day:0>2}.{now.month:0>2}.{now.year}"
    if date2 != date1:
        date1 = date2
        return date2
    else:
        return "NO"


while True:
    t = tick()
    if t != "NO": 
        client(UpdateProfileRequest(last_name=f"YOUR PROFILE NAME {time2}"))
        client(DeletePhotosRequest(client.get_profile_photos('me')))
        result = client(UploadProfilePhotoRequest(file=client.upload_file('profile.png')))
    d=date()
    if d != "NO":
        client(UpdateProfileRequest(about=f"YOUR_BIO {d} 🗓"))

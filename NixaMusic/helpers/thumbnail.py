import os
import random

import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageFont

themes = ["rrc", "hejo", "black"]


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def gen_thumb(thumbnail, title, userid, ctitle):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open(
                    f"NixaMusic/resources/thumb{userid}.png", mode="wb"
                )
                await f.write(await resp.read())
                await f.close()
    theme = random.choice(themes)
    image1 = Image.open(f"NixaMusic/resources/thumb{userid}.png")
    image2 = Image.open(f"NixaMusic/resources/{theme}.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save(f"NixaMusic/resources/temp{userid}.png")
    img = Image.open(f"NixaMusic/resources/temp{userid}.png")
    draw = ImageDraw.Draw(img)
    img.save(f"NixaMusic/resources/final{userid}.png")
    os.remove(f"NixaMusic/resources/temp{userid}.png")
    os.remove(f"NixaMusic/resources/thumb{userid}.png")
    final = f"NixaMusic/resources/final{userid}.png"
    return final

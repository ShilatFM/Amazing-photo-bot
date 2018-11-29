import PIL
import cloudinary

# import PyImage as PyImage

from PIL import Image,ImageOps, ImageEnhance
def new_Greeting(im):
    target_img = Image.new("RGB", (300, 600), "THISTLE")
    out = im.convert("RGB", (
        0.986542, 0.154789, 0.756231, 0,
        0.212671, 0.715160, 0.254783, 0,
        0.123456, 0.119193, 0.112348, 0))
    out.save("Image.jpg")
    o = Image.blend(im, out, 0.5)

    o = o.resize((300, 200))

    target_img.paste(o, (0, 400))
    return target_img



im = Image.open('image2.jpg')
target = new_Greeting(im)
target.show()

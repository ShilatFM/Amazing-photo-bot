import PIL

from PIL import Image,ImageOps
def createGreetingCard(im):
    target_img = Image.new("RGB", (600, 600), "GAINSBORO")
    im = PIL.Image.open(im)

    out = im.convert("RGB", (
        0.412453, 0.357580, 0.180423, 0,
        0.212671, 0.715160, 0.072169, 0,
        0.019334, 0.119193, 0.950227, 0))
    out.save("Image2.jpg")

    out2 = im.convert("RGB", (
        0.9756324, 0.154789, 0.180423, 0,
        0.212671, 0.715160, 0.254783, 0,
        0.123456, 0.119193, 0.950227, 0))
    out2.save("Image3.jpg")

    out3 = im.convert("1")
    out3.save("Image4.jpg")

    out4 = im.convert("RGB", (
        0.986542, 0.154789, 0.756231, 0,
        0.212671, 0.715160, 0.254783, 0,
        0.123456, 0.119193, 0.112348, 0))
    out4.save("Image5.jpg")

    out5 = Image.blend(im, out4, 0.5)
    # out6=out5.rectangle((100, 100, 300, 150), fill=(0, 0, 0, 0))

    out5.save("Image6.jpg")
    #
    # im = bpy.data.images.new("albedo", width=1024, height=1024, alpha=True)
    # im.generated_color = (1, 0, 0, 0.5)
    out6 = out5
    out6.putalpha(128)
    out6.save("Image7.png")
    canvas = PyImage.new('RGBA', out6.size, (255, 255, 255, 255))  # Empty canvas colour (r,g,b,a)
    canvas.paste(out6, mask=out6)  # Paste the image onto the canvas, using it's alpha channel as mask
    canvas.thumbnail([width, height], PyImage.ANTIALIAS)
    canvas.save("out8", format="PNG")

    target_img.save('GreetingCard.jpg')

createGreetingCard('test_collage1.jpg')

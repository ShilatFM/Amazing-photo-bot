import shutil
import gridfs
from pymongo import mongo_client
import urllib.request
from mergeimage import create_collage

c = mongo_client.MongoClient()
db = c.botPhotos
fs = gridfs.GridFS(db)

def save_image(path, c_id):
   fs.put(path.encode('ascii'), chat=c_id, filename=f"{c_id}.jpg")




from PIL import Image
import requests
from io import BytesIO

def load_image(c_id):

    im =[]
    for grid_out in fs.find({"chat": c_id}):
        file = grid_out.read()
        response = requests.get(file.decode("utf-8", "ignore"))
        im.append(Image.open(BytesIO(response.content)))
    print(im)




# def load_image(c_id):
#    num = 0
#    for grid_out in fs.find({"chat": c_id}):
#        # destination = rf"C:\Users\RENT\Desktop\a\{num}.jpg"
#        file = grid_out.read()
#        print(file)
#        urllib.request.urlretrieve(file.decode("utf-8", "ignore"), rf"C:\Users\RENT\Desktop\a\{num}.jpg")
#        num += 1


# save_image(r"C:\Users\RENT\Desktop\vvv.jpg", 7)

print(load_image(701845915))
# create_collage(load_image(701845915)).save("mycolage.jpg")

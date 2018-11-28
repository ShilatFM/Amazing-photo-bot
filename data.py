import gridfs
from pymongo import mongo_client
import PIL

c = mongo_client.MongoClient()
db = c.botPhotos
fs = gridfs.GridFS(db)

def save_image(path, c_id):
   fs.put(path.encode('ascii'), chat=c_id, filename=f"{c_id}.jpg")

def load_image(c_id):
    im = []
    photos = []
    for grid_out in fs.find({"chat": c_id}):
        file = grid_out.read()
        im.append(file.decode("utf-8", "ignore"))
        photos.append(PIL.Image.open('asd.jpg'))
    return photos
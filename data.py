import shutil
import gridfs
from pymongo import mongo_client

c = mongo_client.MongoClient()
db = c.botPhotos
fs = gridfs.GridFS(db)

def save_image(path, c_id):
   fs.put(path.encode('ascii'), chat=c_id, filename=f"{c_id}.jpg")


# def load_image(c_id):
#    num = 0
#    for grid_out in fs.find({"chat": c_id}):
#        destination = rf"C:\Users\RENT\Desktop\a\{num}.jpg"
#        file = grid_out.read()
#        print(file)
#        shutil.copyfile(file, destination)
#
#
# # save_image(r"C:\Users\RENT\Desktop\abc", 7)
# load_image(7)





def load_image():
   destination = rf"C:\Users\RENT\Desktop\a\vvv.jpg"
   for grid_out in fs.find({"chat": 13}):
       file = grid_out.read()
       shutil.copyfile(file, destination)

   # python = Image.open(r"C:\Users\RENT\Downloads\qqq.jfif")
   # dota = Image.open(r"C:\Users\RENT\Downloads\fjords.jpg")
   # Image.alpha_composite(dota, python)

save_image("C:\\Users\\RENT\\Desktop\\vvv", 13)
load_image()
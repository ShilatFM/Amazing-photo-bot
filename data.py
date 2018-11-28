import gridfs
from pymongo import mongo_client

c = mongo_client.MongoClient()
db = c.botPhotos
fs = gridfs.GridFS(db)

def save_image(path, c_id):
   fs.put(path.encode('ascii'), chat=c_id, filename=f"{c_id}.jpg")


# def load_image(name):
#    c = mongo_client.MongoClient()
#    db = c.myImages2
#    fs = gridfs.GridFS(db)
#    destination = rf"C:\Users\RENT\Desktop\python\acaton\{name}.jpg"
#    for grid_out in fs.find({"name": b"giti555"}):
#        file = grid_out.read()
#        shutil.copyfile(file, destination)



# load_image("jpg")
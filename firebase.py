import pyrebase


class FireBase:
    def __init__(self):
        config = {
            "apiKey": "AIzaSyA06PmLFx-6XEtmKwjOpVVzXeZ7e2nPqqM",
            "authDomain": "testing-906b6.firebaseapp.com",
            "databaseURL": "https://testing-906b6-default-rtdb.asia-southeast1.firebasedatabase.app/",
            "projectId": "testing-906b6",
            "storageBucket": "testing-906b6.appspot.com",
            "messagingSenderId": "168740903247",
            "appId": "1:168740903247:web:71a33cb64dff9f164fcd3a",
            "measurementId": "G-FJVW2T2P4H"
        }

        firebase = pyrebase.initialize_app(config)
        self.database = firebase.database()
        self.storage = firebase.storage()

    def insert_data(self, user, id, data):
        self.database.child(user).child(id).set(data)

    def get_data(self, user, id):
        return self.database.child(user).child(id).get()

    def insert_img(self, user, id, img_path):
        self.storage.child(user).child(id).put(img_path)

    def get_img(self, user, id, out_path, out_name):
        self.storage.child(user).child(id).download(path=out_path, filename=out_name)

    def insert_vid(self, user, id, vid_path):
        self.storage.child(user).child(id).put(vid_path)

    def get_vid(self, user, id, out_path, out_name):
        self.storage.child(user).child(id).download(path=out_path, filename=out_name)


fb = FireBase()

##############  Insert and extract data   ########################
# data = {"Name":"Ram", "Age":25}
# fb.insert_data("pk","firstperson", data)
# output = fb.get_data("pk", "firstperson")
# print(output.val())

# to store the image, first create a bucket. it is present inside build
##############  Insert and extract Image   ########################
# fb.insert_img("pk", "firstImg", "C:/Users/kumar/PycharmProjects/mdb/pk.png")
# fb.get_img("pk", "firstImg", "C:/Users/kumar/PycharmProjects/mdb/", "output.png")

##############  Insert and extract video   ########################
# fb.insert_vid("pk", "firstVid", "C:/Users/kumar/PycharmProjects/mdb/t1.mp4")
# fb.get_vid("pk", "firstVid", "C:/Users/kumar/PycharmProjects/mdb/", "output.mp4")

import pyrebase
from dotenv import load_dotenv
import os

load_dotenv()
firebase_config={
     "apiKey":os.getenv("apiKey") ,
  "authDomain": os.getenv("authDomain"),
  "projectId":os.getenv("projectId"),
  "storageBucket":os.getenv("storageBucket") ,
  "messagingSenderId": os.getenv("messagingSenderId"),
  "appId":os.getenv("appId") ,
  "measurementId":os.getenv("measurementId"),
  "databaseURL":os.getenv("databaseURL")
}


firebase=pyrebase.initialize_app(firebase_config)
db=firebase.database()
data={"name":"Barış","surname":"Karakulak","age":21}


db.child("Barış").set(data)
# db몽고 사이트를 원격으로 바꾸는 연습

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:test@cluster0.gp0cqjt.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)

db = client.dbsparta


movie = db.movies.find_one({'title':'가버나움'})
target_star = movie['star']


movies = list(db.movies.find({'star': target_star },{'_id':False}))
for a in movies :
    print(a['title'])

db.movies.update_one({'title':'가버나움'},{'$set':{'star':0}})
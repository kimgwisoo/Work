from pymongo import MongoClient
client = MongoClient()
# 클래스 객체 할당


client = MongoClient('127.0.0.1', 27017)
# localhost : ip주소
# 27017: port 번호



####DB계정에 비번이 걸려있거나 외부 IP인 경우, 다음과 같이 연결
####DB_HOST = 'xxx.xxx.xxx.xxx:27017'
####DB_ID = 'root'
####DB_PW = 'PW'

####client = MongoClient('mongodb://%s:%s@%s' % (DB_ID,DB_PW,DB_HOST))




db = client["DB_이름"]
# db의 이름을 문자열로 할당 받기


import traceback
import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://omenxd234:Abcd1234@cluster0.iq5ar.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
result = str(client)

if "connect=True" in result:
    try:
        print("MONGODB CONNECTED SUCCESSLY ✅")
    except:
        pass
else:
    try:
        print("MONGODB CONNECTION FAILED ❌")
    except:
        pass

folder = client["XCC_DATABASE"]
usersdb = folder.USERSDB
chats_auth = folder.CHATS_AUTH
gcdb = folder.GCDB
sksdb = client["SKS_DATABASE"].SKS
import pymongo
import dns
import sys


def query(collection, uid):
    return(collection.find_one({"uid": uid})["num_box"])

def update(collection, uid, inc_val):
    collection.update_one({"uid" : uid}, {"$inc": {"num_box" : inc_val}})
    return query(collection, uid)
def new(collection, uid):
    collection.insert_one({"uid" : uid, "num_box" : 0})


client = pymongo.MongoClient("mongodb+srv://spark9312:hackathon_SungJun@hackathon-dnqp6.azure.mongodb.net/test?retryWrites=true")
db = client.user_db
col = db.user

# # Add new User
# # collection.insert_one({"_id" : "F0007Q1", "num_box" : 0})
# if (len(sys.argv) == 3):
#     # Box returned
#     if (sys.argv[1] == "return"):
#         update(col, sys.argv[2], 1)
#         print("You have {} boxes remaining".format(query(col, sys.argv[2])))
#     # Box used
#     if (sys.argv[1] == "use"):
#         update(col, sys.argv[2], -1)
#         print("You have {} boxes remaining".format(query(col, sys.argv[2])))
#
#     # Query how man box a user has
#     if (sys.argv[1] == "query"):
#         print("You have {} boxes remaining".format(query(col, sys.argv[2])))
#
# else:
#     print("This program requires two parameters: <Mode: return, use, query> <User ID>")

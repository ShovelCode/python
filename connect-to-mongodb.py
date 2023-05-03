import pymongo

# Set up the MongoDB client
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Connect to a specific database
mydb = client["mydatabase"]

# Create a new collection
mycol = mydb["customers"]

# Insert a new document into the collection
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

# Print the ID of the inserted document
print(x.inserted_id)

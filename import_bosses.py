import json
from pymongo import MongoClient
import os

# Replace with your MongoDB Atlas connection string
MONGO_URI = os.environ.get("MONGO_URI")  # We'll set this in Vercel later
if not MONGO_URI:
    MONGO_URI = "mongodb+srv://keenlyien:admin12345@bosstracker.alqsb9c.mongodb.net/?appName=BossTracker"

client = MongoClient(MONGO_URI)
db = client.bossTracker
collection = db.bosses

# Load JSON data
with open("data/bosses.json", "r", encoding="utf-8") as f:
    bosses = json.load(f)

# Optional: clear existing collection
collection.delete_many({})

# Insert all bosses
collection.insert_many(bosses)

print(f"Imported {len(bosses)} bosses into MongoDB Atlas!")

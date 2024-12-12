
from pymongo import MongoClient

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://Anusha_venkat:Dickite3036@cluster0.h3q4j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["web_scraping_db"]  # Access the database
collection = db["query_data"]  # Access the collection

# Fetch and print all documents in the collection
def verify_stored_data():
    documents = collection.find()  # Retrieve all documents from the collection
    print("Stored Data in MongoDB:")
    for doc in documents:
        print(f"Link: {doc['link']}")
        print(f"Query: {doc['query']}")
        print("Relevant Data:")
        for item in doc['relevant_data']:
            print(f"- {item}")
        print("\n")

if __name__ == "__main__":
    verify_stored_data()

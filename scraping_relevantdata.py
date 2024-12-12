import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


# MongoDB Atlas connection
client = MongoClient("mongodb+srv://Anusha_venkat:Dickite3036@cluster0.h3q4j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["web_scraping_db"]
collection = db["query_data"]

def scrape_relevant_data(links, query):
    query_results = []
    for link in links:
        try:
            # Fetch the webpage
            page = requests.get(link, timeout=10)
            page.raise_for_status()

            # Parse HTML content
            soup = BeautifulSoup(page.text, 'html.parser')

            # Search for relevant text based on query
            relevant_data = []
            for tag in soup.find_all(['h1', 'h2', 'h3', 'p', 'li']):  # Search in headings, paragraphs, and lists
                if query.lower() in tag.get_text(strip=True).lower():
                    relevant_data.append(tag.get_text(strip=True))

            # If relevant data is found, store it
            if relevant_data:
                data = {
                    "link": link,
                    "query": query,
                    "relevant_data": relevant_data
                }
                query_results.append(data)
                collection.insert_one(data)  # Store in MongoDB
        except Exception as e:
            print(f"Error processing {link}: {e}")
    return query_results

if __name__ == "__main__":
    # Input from the user
    links = [
        "https://www.manipal.edu/mit/why/industry-partnership.html",
        "https://www.manipal.edu/scholarships"
    ]
    query = input("Enter your query: ")

    # Fetch relevant data
    results = scrape_relevant_data(links, query)

    # Print the results
    for result in results:
        print(f"Link: {result['link']}")
        print("Relevant Data:")
        for item in result['relevant_data']:
            print(f"- {item}")
        print("\n")
import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer, util

API_KEY = "AIzaSyBF4hG2n8CfMxwOWlBjGSS7Ey9wQYuhyhM" #Google API Key
CX = "e0a6f838c9a544be1" #Custom Search Engine ID

def google_search_urls(query, num_results=30):
    search_results = []  # List to store webpage URLs
    query = query.replace(" ","+")
    for start in range(1, num_results, 10):  # Google API returns results in batches of 10
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CX}&start={start}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for item in data.get("items", []):
                search_results.append(item["link"])  # Extract full webpage URL
        else:
            # print("Error:", response.json())
            break
    return search_results  # Return the complete list of webpage URLs

# Example 
# query = "13 Of World's 20 Most Polluted Cities In India, Delhi Most Polluted Capital"
# top_webpages = google_search_urls(query)
# print(top_webpages)




def scrape_titles(websites, max_titles=30):
    titles = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    for website in websites:
        if len(titles) >= max_titles:
            break  # Stop when we have enough titles
        
        try:
            response = requests.get(website, headers=headers, timeout=5)
            response.raise_for_status()  # Check if request was successful
            
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.find("title").get_text(strip=True)  # Extract page title
            
            if title:  # Ensure the title is valid
                titles.append(title)

        except Exception as e:
            pass  # Skip if any error occurs

    return titles  # Only return list of titles



# scraped_titles = scrape_titles(top_webpages)

# print(scraped_titles)
# print(len(scraped_titles))

#!pip install sentence-transformers





def calculate_similarity_bert(input_title, title_list, threshold=0.6):
    model = SentenceTransformer("all-MiniLM-L6-v2")  # Load pre-trained Sentence Transformer model
    input_embedding = model.encode(input_title, convert_to_tensor=True)  # Convert input title to vector
    title_embeddings = model.encode(title_list, convert_to_tensor=True)  # Convert all list titles to vectors
    # print(input_embedding)
    # print(title_embeddings)

    # Compute cosine similarity between input title and each title in the list
    similarity_scores = util.pytorch_cos_sim(input_embedding, title_embeddings)[0].tolist()
    
    avg_similarity = sum(similarity_scores) / len(similarity_scores) if similarity_scores else 0  # Compute average score

    # print(f"Average Similarity Score: {avg_similarity:.2f}")
    
    return "Real News" if avg_similarity >= threshold else "Fake News"

# Example usage
# input_title = query
# title_list = scraped_titles

# result = calculate_similarity_bert(input_title, title_list)
# print(result)


def check_real(query):
    top_webpages = google_search_urls(query)
    scraped_list = scrape_titles(top_webpages)
    out = calculate_similarity_bert(query,scraped_list)
    return False if out=="Fake News" else True

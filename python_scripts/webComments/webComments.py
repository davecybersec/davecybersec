import requests
from bs4 import BeautifulSoup
from bs4.element import Comment

# URL of the web page you want to scrape comments from
url = input("Enter a complete URL (https://<URL>): ")

# Send a GET request to fetch the web page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all comments in the HTML
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    
    # Print out each comment
    for idx, comment in enumerate(comments, start=1):
        print(f"Comment {idx}: {comment}")
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")

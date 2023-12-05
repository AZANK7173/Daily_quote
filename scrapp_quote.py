import requests
from bs4 import BeautifulSoup

def get_content_from_link(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the content you need using BeautifulSoup methods
            # For example, printing the page title
            author = soup.item.title.text
            quote = soup.item.description.text

            return author, quote

        else:
            return response.status_code

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    # Replace 'your_url_here' with the actual URL you want to scrape
    url_to_scrape = 'https://www.quotedb.com/quote/quote.php?action=quote_of_the_day_rss'
    tup = get_content_from_link(url_to_scrape)

    print(tup[0])
    print(tup[1])


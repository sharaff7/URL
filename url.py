import requests

class URLShortener:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api-ssl.bitly.com/v4/shorten"

    def shorten_url(self, long_url):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        payload = {
            "long_url": long_url,
            "domain": "bit.ly",  # You can customize this based on your preference
        }

        try:
            response = requests.post(self.base_url, json=payload, headers=headers)
            response.raise_for_status()  # Check for HTTP errors

            return response.json()["id"]
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Request Error: {err}")

        return None

# Replace 'your_api_key' with your actual Bitly API key
bitly_api_key = 'b6e205afdab864c9afec9409afea6b187b54151e'
url_shortener = URLShortener(bitly_api_key)

# Example: Shorten a URL
long_url = "https://www.example.com"
short_url = url_shortener.shorten_url(long_url)

if short_url:
    print(f"Original URL: {long_url}")
    print(f"Shortened URL: {short_url}")
else:
    print("Failed to shorten URL. Please check your API key.")

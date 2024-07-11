import requests

def download_with_retry(urls):
  results = []
  for url in urls:
    for i in range(3):
      try:
        response = requests.get(url)
        response.raise_for_status()
        results.append(response.content)
        break
      except requests.exceptions.RequestException as e:
        print(f"Error while downloading {url}: {e}")
        if i == 2:
          print(f"Failed to download {url} after 3 retries.")
          return None
  return results
urls = [
    "www.google.com",
]

downloaded_content = download_with_retry(urls)

if downloaded_content:
  for content in downloaded_content:
    print(f"Downloaded content: {content[:50]}...")
else:
  print("Failed to download any files.")

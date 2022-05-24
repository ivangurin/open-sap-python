import requests

search_text = input("Please enter a search term: ")

reqsuest = requests.get(
    f"https://itunes.apple.com/search?term={search_text}&entity=album")

result = reqsuest.json()

print(f"The search returned { result['resultCount'] } results.")

for album in result["results"]:
    print(
        f"Artist: { album['artistName'] } - Album: { album['collectionName'] } - Track Count: { album['trackCount'] }")

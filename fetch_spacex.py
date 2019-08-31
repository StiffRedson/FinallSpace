from os.path import join as joinpath
import requests
import json
import os


def fetch_spacex_last_launch():
    payload = {
        "filter": "links"
    }
    response = requests.get(url="https://api.spacexdata.com/v3/launches/latest", params=payload)
    photo_links = json.loads(response.text)
    print(photo_links)
    urls = photo_links["links"]["flickr_images"]
    print(urls)

    os.makedirs('imagesX', exist_ok=True)

    for num, url in enumerate(urls, 1):
        response = requests.get(url)
        response.raise_for_status()
        photo_name = f'SpaceX_{str(num)}.jpg'
        print(photo_name)

        path = os.path.abspath('imagesX')
        photo_path = joinpath(path, photo_name)
        print(photo_path)

        with open(photo_path, 'wb') as photo:
            photo.write(response.content)


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()

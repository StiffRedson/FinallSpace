import requests
import json
import os
from os.path import join as joinpath


def fetch_spacex_last_launch():
    payload = {
        "filter": "links"
    }
    response = requests.get(url="https://api.spacexdata.com/v3/launches/latest", params=payload)
    photo_links = json.loads(response.text)
    urls = photo_links["links"]["flickr_images"]

    if not os.path.exists('imagesX'):
        os.makedirs('imagesX')

    for num, url in enumerate(urls, 1):
        response = requests.get(url)
        response.raise_for_status()
        photo_name = 'SpaceX_' + str(num) + '.jpg'

        photo_path = joinpath(os.path.abspath('imagesX'), photo_name)

        with open(photo_path, 'wb') as file:
            file.write(response.content)


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()

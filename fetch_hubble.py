import argparse
from urllib.parse import urlparse
from os.path import join as joinpath
import requests
import json
import os

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-c', type=str, help="collection name")
parser.add_argument('-n', type=int, help="number photo")
args = parser.parse_args()


def fetch_hubble_collection(id_photo):
    url_template = "http://hubblesite.org/api/v3/image/{}"
    url_photo_id = url_template.format(id_photo)
    response_id_photo = requests.get(url_photo_id)
    response_id_photo.raise_for_status()
    links_photo = json.loads(response_id_photo.text)
    print(f'loading ... id{id_photo}')
    photos = links_photo['image_files']
    data_photos = {'description': dict(id=id_photo, name=links_photo['name'])}
    links = {}
    for num, photo in enumerate(photos):
        name_photo = 'Hubble_id{}'.format(id_photo)
        split = urlparse(photo.get('file_url'))
        split_netloc = split[1].split('.')[1:]
        split_path = split[2].split('/')[2:]
        link = f"http://{'.'.join(split_netloc)}/{'/'.join(split_path)}"
        links[num] = link
    data_photos[name_photo] = links
    response = requests.get(data_photos[name_photo][args.n])
    response.raise_for_status()

    os.makedirs('imagesH', exist_ok=True)

    expansion_photo = data_photos[name_photo][args.n].split('.')[-1]
    image_name = f'Hubble_id{id_photo}_{str(args.n)}.{expansion_photo}'
    image_path = joinpath(os.path.abspath('imagesH'), image_name)
    data_photos['description']['path'] = image_name

    with open(image_path, 'wb') as image:
        image.write(response.content)

    return data_photos


def get_id_photo(collection):
    url = "http://hubblesite.org/api/v3/images"

    payload = {
        "page": "all",
        "collection_name": collection
    }

    response = requests.get(url, payload)
    response.raise_for_status()

    id_collection = []
    for image_id in response.json():
        id_image = image_id["id"]
        id_collection.append(id_image)
    return id_collection


def main():
    collection = args.c
    json_data = []
    for index in get_id_photo(collection):
        json_data.append(fetch_hubble_collection(index))
        with open("info_photo.json", 'w') as file:
            json.dump(json_data, file, indent=2)


if __name__ == "__main__":
    main()

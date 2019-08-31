import argparse
import json
import os
import time
from os import listdir
from os.path import isfile
from os.path import join as joinpath
from dotenv import load_dotenv
from instabot import Bot


def create_parser():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-folder', type=str, help="folder name")
    args = parser.parse_args()
    return args.folder


def main():
    timeout = 60
    my_path = create_parser()

    load_dotenv()
    username = os.getenv("INSTAGRAM_USERNAME")
    password = os.getenv("INSTAGRAM_PASSWORD")

    bot = Bot()
    bot.login(username=username, password=password)

    try:
        if my_path == 'imagesX':
            for image in listdir(my_path):
                if isfile(joinpath(my_path, image)):
                    photo_path = joinpath(my_path, image)
                    caption = "The last launch of the Shuttle company 'SpaceX'"
                    bot.upload_photo(photo_path, caption=caption)

                    if bot.api.last_response.status_code != 200:
                        print(bot.api.last_response)
                        break

                    time.sleep(timeout)
        else:
            with open('info_photo.json', 'r') as f:
                data = json.load(f)
                for image in data:
                    photo_path = joinpath(my_path, image['description']['path'])
                    caption = str(image['description']['name'])

                    print("upload: " + caption)
                    bot.upload_photo(photo_path, caption=caption)

                    if bot.api.last_response.status_code != 200:
                        print(bot.api.last_response)
                        break

                    time.sleep(timeout)

    except Exception as error:
        print(str(error))
    time.sleep(60)


if __name__ == '__main__':
    main()

import argparse
import json
import os
import sys
import time
from os import listdir
from os.path import isfile
from os.path import join as joinpath
from dotenv import load_dotenv

from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-folder', type=str, help="folder name")
args = parser.parse_args()

my_path = args.folder
timeout = 60


def main():

    if USERNAME is None:
        sys.exit('[*]check the correctness of the login or password')
    if PASSWORD is None:
        sys.exit('[*]check the correctness of the login or password')
    try:
        if my_path == 'imagesX':
            for image in listdir(my_path):
                if isfile(joinpath(my_path, image)):
                    photo_path = joinpath(my_path, image)
                    caption = "The last launch of the Shuttle company 'SpaceX'"
                    bot.upload_photo(photo_path, caption=caption)

                    if bot.api.last_response.status_code != 200:
                        print(bot.api.last_response)
                        # snd msg
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
                        # snd msg
                        break

                    time.sleep(timeout)

    except Exception as error:
        print(str(error))
    time.sleep(60)


if __name__ == '__main__':
    load_dotenv()
    USERNAME = os.getenv("INSTAGRAM_USERNAME")
    PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
    bot = Bot()
    bot.login(username=USERNAME, password=PASSWORD)
    main()

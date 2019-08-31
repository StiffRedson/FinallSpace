from PIL import Image
import argparse
import os
from os.path import join as joinpath


def create_parser():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-x1', type=float, help="offset left x1")
    parser.add_argument('-y1', type=float, help="offset up y1")
    parser.add_argument('-x2', type=float, help="offset right x2")
    parser.add_argument('-y2', type=float, help="offset down y2")
    parser.add_argument('-folder', type=str, help="folder name")
    args = parser.parse_args()
    return args.x1, args.y1, args.x2, args.y2, args.folder


def resize_image(photo_name, offset_x1, offset_y1, offset_x2, offset_y2, folder_id):
    path_initial = os.path.abspath(f'images{folder_id}')
    original_image = Image.open(joinpath(path_initial, photo_name))
    width, height = original_image.size
    print('The original image size is {wide} wide x {height}'
          'high'.format(wide=width, height=height))

    xcenter = original_image.width/2
    ycenter = original_image.height/2
    x1 = xcenter - offset_x1
    y1 = ycenter - offset_y1
    x2 = xcenter + offset_x2
    y2 = ycenter + offset_y2
    area = (x1, y1, x2, y2)
    reform_image = original_image.crop(area)
    width, height = reform_image.size
    print('The reform image size is {wide} wide x {height}'
          'high'.format(wide=width, height=height))
    reform_image.show()
    destination_path = os.path.abspath('resize_image')
    reform_image.save(joinpath(destination_path, photo_name))


def main():
    step_left = create_parser()[0]
    step_up = create_parser()[1]
    step_right = create_parser()[2]
    step_down = create_parser()[3]
    index_folder = create_parser()[4]
    directory = os.path.abspath(f'images{index_folder}')
    listing = os.listdir(directory)
    listing.sort()
    os.makedirs('resize_image', exist_ok=True)
    for file_path in listing:
        resize_image(file_path, step_left, step_up, step_right, step_down, index_folder)


if __name__ == '__main__':
    main()

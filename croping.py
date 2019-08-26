from PIL import Image
import argparse
import os

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-x1', type=float, help="coordinate x1")
parser.add_argument('-y1', type=float, help="coordinate y1")
parser.add_argument('-x2', type=float, help="coordinate x2")
parser.add_argument('-y2', type=float, help="coordinate y2")
parser.add_argument('-folder', type=str, help="folder name")
args = parser.parse_args()


def resize_image(path):
    original_image = Image.open(os.path.abspath(f'images{args.folder}') + '/' + path)
    print(original_image)
    width, height = original_image.size
    print('The original image size is {wide} wide x {height}'
          'high'.format(wide=width, height=height))

    xcenter = original_image.width/2
    ycenter = original_image.height/2
    x1 = xcenter - args.x1
    y1 = ycenter - args.y1
    x2 = xcenter + args.x2
    y2 = ycenter + args.y2
    area = (x1, y1, x2, y2)
    reform_image = original_image.crop(area)
    width, height = reform_image.size
    print('The reform image size is {wide} wide x {height}'
          'high'.format(wide=width, height=height))
    reform_image.show()
    reform_image.save(os.path.abspath('resize_image') + '/' + path)


def main():
    directory = os.path.abspath(f'images{args.folder}')
    listing = os.listdir(directory)
    listing.sort()
    if not os.path.exists('resize_image'):
        os.makedirs('resize_image')
    for file_path in listing:
        resize_image(file_path)


if __name__ == '__main__':
    main()

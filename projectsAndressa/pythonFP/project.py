import os
from PIL import Image
from PIL import ImageFilter
import numpy as np
import cv2
import csv
import time


def main():
    folder = "images/"

    print("After upload the image on the folder images ..please, type the image name and see the magic happens!")
    img = input("Image name: ")
    img_folder = "images/" + img

    a, e = img.split(".")

    if (e != "jpg"):
        raise Exception("Sorry, file is not a .jpg")
    else:
        if (os.path.exists(img_folder) == False):
            raise Exception("File does not exist.")
        else:
            img_gray()
            img_sharpen(img_folder)
            img_edges(img_folder)

    files = os.listdir(folder)

    with open("analysis.csv", "w") as analysis:
        writer = csv.DictWriter(analysis, fieldnames=["name", "brightness", "avgColor", "brightnessRange", "size"])
        writer.writeheader()
        for file in files:
            brit = brightness(file)
            brit_r = brightness_range(file)
            c_avg = color_avg(file)
            img_s = img_size(file)
            writer.writerow(
                {
                    "name":file,
                    "brightness": brit,
                    "avgColor": c_avg,
                    "brightnessRange": brit_r,
                    "size": img_s
                }

            )
    print("Done .. please go to the images folder to see what images was generated based in the image submitted and also, see the analysis file with more information about all the images. Enjoy!!")

def wait_image_generated(image_path,timeout=60, check_interval=1):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if os.path.exists(image_path):
            return True
        time.sleep(check_interval)
    return False


def img_sharpen(img):
    with Image.open(img) as imageS:
        imageS = imageS.filter(ImageFilter.SHARPEN)
        imageS.save("images/imageSharpen.jpg")

        image_file_path = "images/imageSharpen.jpg"
        if wait_image_generated(image_file_path):
            print(f"Image '{image_file_path}' has been generated.")
        else:
            print(f"Timeout.")

def img_edges(img):
    with Image.open(img) as image_e:
        image_e = image_e.filter(ImageFilter.FIND_EDGES)
        image_e.save("images/imageEdges.jpg")

    image_file_path = "images/imageEdges.jpg"
    if wait_image_generated(image_file_path):
        print(f"Image '{image_file_path}' has been generated.")
    else:
        print(f"Timeout.")


def img_gray():
    file_name_list = glob("images/*.jpg")
    file2 = cv2.imread(file_name_list[0])
    gray = cv2.cvtColor(file2, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("images/grayImage.jpg",gray)

    image_file_path = "images/grayImage.jpg"
    if wait_image_generated(image_file_path):
        print(f"Image '{image_file_path}' has been generated.")
    else:
        print(f"Timeout.")

def brightness(img):
    with Image.open("images/" + img) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness

def brightness_range(img):
    img_r=np.array(Image.open("images/" + img).convert("L"))
    min=np.min(img_r)
    max=np.max(img_r)
    return min, max

def color_avg(img):
    np.seterr(over='ignore')
    img_avg=np.array(Image.open("images/" + img).convert("L"))
    minimumColor = np.amin(img_avg)
    maximumColor = np.amax(img_avg)
    return (minimumColor - maximumColor)/2

def img_size(img):
    with Image.open("images/" + img) as image:
        size = image.size
    return size

if __name__ == "__main__":
    main()

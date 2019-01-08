from PIL import Image
import numpy as np
import cv2
# image = Image.open('segnet_output/b1c9c847-3bda4659.jpg')
# print(np.unique(image))
# image.putalpha(75)  # Half alpha; alpha argument must be an int
# image.save("segnet_output/segnet_output_alpha/b1c9c847-3bda4659.png")
with open("nopeTest.txt") as f:
    for line in f:
        im1_path, im2_path = line.split()
        overlay = cv2.imread(im1_path)
        background = cv2.imread(f"../bdd100k/bdd100k/images/{im1_path}")


        background = cv2.resize(background, (overlay.shape[1], overlay.shape[0]))
        if background is None:
            print('nope')
            continue
        if overlay is None:
            print("nopenope")
            continue
        print(im1_path)

        added_image = cv2.addWeighted(background,1.0,overlay,0.4,0)
        added_image = cv2.resize(added_image, (640, 360))
        cv2.imwrite(f'output/{im1_path}', added_image)
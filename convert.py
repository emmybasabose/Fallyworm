import os

import cv2
import glob

for filename in glob.glob(r'C:\\Users\\BWAMIKI ISAAC Jr\\PycharmProjects\\FallyWorm\\original_images*.jpg'):
    print(filename)
    img = cv2.imread(filename)
    rl = cv2.resize(img, (500, 500))
    cv2.imshow('Original Images', rl)
    cv2.waitKey(0)
    gray_image = cv2.cvtColor(rl, cv2.COLOR_BGR2GRAY)
    # x=cv2.imwrite(f'{filename}\\converted.jpg', gray_image)
    x = cv2.imwrite(f'C:\\Users\\BWAMIKI ISAAC Jr\\PycharmProjects\\FallyWorm\original_images\\converted\\{os.path.basename(filename)}',gray_image)
    cv2.imshow("Converted Images", x)
    cv2.destroyAllWindows()

import numpy as np
import imageio
import cv2
import scipy.ndimage

IMAGE_NAME = "images/NITK Beach"
IMAGE_EXTENSION = ".jpg"
original_image = imageio.imread(IMAGE_NAME + IMAGE_EXTENSION)

def grayscale(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])

def dodge(front, back):
    result = (front*255) / (255-back)
    result[result>255] = 255
    result[back==255] = 255
    return result.astype('uint8')

gray_image_1 = grayscale(original_image)
gray_image_2 = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

inverted_image_1 = 255 - gray_image_1
inverted_image_2 = 255 - gray_image_2

blur_image_1 = scipy.ndimage.filters.gaussian_filter(inverted_image_1, sigma=100)
blur_image_2 = cv2.GaussianBlur(inverted_image_2, (21,21), 0)

inverted_blur_image = 255 - blur_image_2

final_image_1 = dodge(blur_image_1, gray_image_1)
final_image_2 = cv2.divide(gray_image_2, inverted_blur_image, scale=256.0)
final_image_3 = cv2.stylization(original_image, sigma_s=150, sigma_r=0.25)

cv2.imwrite(IMAGE_NAME + " - Sketch1" + IMAGE_EXTENSION, final_image_1)
cv2.imwrite(IMAGE_NAME + " - Sketch2" + IMAGE_EXTENSION, final_image_2)
cv2.imwrite(IMAGE_NAME + " - Sketch3" + IMAGE_EXTENSION, final_image_3)

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math


# Image load
image = mpimg.imread('solidWhiteCurve.jpg')

# global variable (width, height, color)
# 800, 450, 3
height, width, color = image.shape
print('width:  ', width)
print('height: ', height)
print('channel:', color)


region_of_interest_vertices = [
    (0, height),
    # 600 / 2 = 400
    # 450 / 2 = 225
    # flot 형태.
    (width / 2, height / 2),
    (width, height),
]

print(region_of_interest_vertices[1])

# region_of_interest funtion

# John F. Canny invented an algorithm to do just that,


def region_of_interest(img, vertices):

    # 빈행렬을 정의한다 height / width
    mask = np.zeros_like(img)

    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_lines(img, lines, color=[255, 0, 0], thickness=3):
    # If there are no lines to draw, exit.
    if lines is None:
        return
    # Make a copy of the original image.
    img = np.copy(img)
    # Create a blank image that matches the original in size.
    line_img = np.zeros(
        (
            img.shape[0],
            img.shape[1],
            3
        ),
        dtype=np.uint8,
    )
    # Loop over all lines and draw them on the blank image.
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_img, (x1, y1), (x2, y2), color, thickness)
    # Merge the image with the lines onto the original.
    img = cv2.addWeighted(img, 0.8, line_image, 1.0, 0.0)
    # Return the modified image.
    return img


# 원본 이미지
plt.figure()
plt.imshow(image)
plt.show()

gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cannyed_image = cv2.Canny(gray_image, 100, 200)

cropped_image = region_of_interest(
    cannyed_image,
    np.array(
        [region_of_interest_vertices],
        np.int32
    ),
)

lines = cv2.HoughLinesP(
    cropped_image,
    rho=6,
    theta=np.pi / 60,
    threshold=160,
    lines=np.array([]),
    minLineLength=40,
    maxLineGap=25
)

line_image = draw_lines(image, lines)  # <---- Add this call.

plt.figure()
plt.imshow(line_image)
plt.show()

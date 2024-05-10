import cv2
import random


image = cv2.imread("")

height, width, channel = image.shape

for i in range(height):
    for j in range(width):
        x = i * random.randint(1,2)
        y = j * random.randint(1,2)
        x = max(0,min(x,height-1))
        y = max(0,min(y,width-1))
        image[i, j] = image[x, y]

cv2.imshow("Noisy image", image)
cv2.waitKey(0)
cv2.destroyAllWindows
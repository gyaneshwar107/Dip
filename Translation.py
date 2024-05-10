import cv2
import numpy as np

# Read the image
image = cv2.imread("IMG_2638kkkkk.jpg")

# Check if the image was loaded successfully
if image is None:
    print("Error: Unable to load the image.")
else:
    # Get image dimensions
    height, width, channels = image.shape

    dx = int(input("Enter the number of units you want to shift your x coordinate: "))
    dy = int(input("Enter the number of units you want to shift your y coordinate: "))

    # Create a blank image with the same dimensions as the original
    shifted_image = np.zeros_like(image)

    for i in range(height):
        for j in range(width):
            # Calculate shifted coordinates
            x = i + dx
            y = j + dy
            
            # Ensure the shifted coordinates are within the image boundaries
            x = max(0, min(x, height - 1))
            y = max(0, min(y, width - 1))
            
            # Update pixel values in the shifted image
            shifted_image[i, j] = image[x, y]

    # Display the shifted image
    cv2.imshow("Shifted Image", shifted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Calculate new center coordinates after shifting
    new_x_centre = height / 2 + dx
    new_y_centre = width / 2 + dy

    print(f"New center of the image is {new_x_centre}, {new_y_centre}")

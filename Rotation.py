import cv2
import math

# Read the image
image = cv2.imread("img.jpg")

# Get image dimensions
height, width, channels = image.shape

# Convert angle from degrees to radians
theta = float(input("Angle of rotation for image in degrees: "))
theta_rad = math.radians(theta)

# Create a blank image to store the rotated image
rotated_image = image.copy()

# Calculate the center point for rotation
center_x = width / 2
center_y = height / 2

# Perform rotation pixel by pixel
for i in range(height):
    for j in range(width):
        # Translate to origin
        #x = i - center_y
        #y = j - center_x
        
        # Rotate
        x_new = i * math.cos(theta_rad) - j * math.sin(theta_rad)
        y_new = i * math.sin(theta_rad) + j * math.cos(theta_rad)
        
        
        # Round the coordinates to integers
        x_new = int(round(x_new))
        y_new = int(round(y_new))
        
        # Check if the new coordinates are within bounds
        if 0 <= x_new < height and 0 <= y_new < width:
            rotated_image[i, j] = image[x_new, y_new]
        else:
            rotated_image[i, j] = 0  # Set to black for out-of-bounds pixels

# Display the rotated image
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
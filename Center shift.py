import cv2

# Read the image
image = cv2.imread("trial.jpeg")

height, width, channels = image.shape

dx = int(input("Enter the number of units you want to shift your x coordinate "))
dy = int(input("Enter the number of units you want to shift your x coordinate "))




for i in range(height):
    for j in range(width):
        x = i + dx
        y = j + dy
        x = max(0, min(x, height - 1))
        y = max(0, min(y, width-1))        
        image[i,j] = image [ x,y] 
# Display the image
        
height, width, channels = image.shape

x_centre = height/2
y_centre = width/2

# Calculate new center coordinates after shifting
new_x_centre = x_centre + dx
new_y_centre = y_centre + dy

print(f"The new centre of the image lies at {new_x_centre}, {new_y_centre}")



 #print(f"The centre of the image lies at {x_centre},{y_centre}")

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
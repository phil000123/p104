import cv2

# Read the image
img = cv2.imread("solar-system.jpg")

# Display the original image
cv2.imshow("output", img)
cv2.waitKey(0)

# Add text below each planet
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.8
font_color = (255, 255, 255)  # White color
font_thickness = 2

# Add text for each planet
cv2.putText(img, "Mercury", (50, 400), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Venus", (200, 400), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Earth", (350, 400), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Mars", (500, 400), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Jupiter", (650, 400), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Saturn", (800, 400), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Uranus", (950, 400), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Neptune", (1100, 400), font, font_scale, font_color, font_thickness)

# Display the image with added text
cv2.imshow("output", img)
cv2.waitKey(0)

# Save the final image with added text
cv2.imwrite("Solar_system_with_names.jpg", img)

# Close all windows
cv2.destroyAllWindows()

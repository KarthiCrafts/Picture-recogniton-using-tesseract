import cv2
import pytesseract

# Set the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load an image using OpenCV
image_path = r'C:\Program Files\Tesseract-OCR\photo with horse.jpg'
#image_path = r'C:\Program Files\Tesseract-OCR\single.jpg'  
#image_path = r'C:\Program Files\Tesseract-OCR\3boyz.jpg'
image = cv2.imread(image_path)


# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image.")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to enhance text visibility (optional)
    _, thresholded_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Use Tesseract to perform character recognition
    recognized_text = pytesseract.image_to_string(thresholded_image)

    # Print the recognized text
    print("Recognized Text:")
    print(recognized_text)

    # Display the original image and thresholded image
    cv2.imshow('Original Image', image)
    cv2.imshow('Thresholded Image', thresholded_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

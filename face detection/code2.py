import cv2

# Path to the Haar Cascade XML file for face detection
HARR_CASCADE_PATH = "model/haarcascade_frontalface_default.xml"

def detect_faces_in_image(image_path):
    """
    Detect faces in a static image and display the result.
    """
    # Load the image
    image = cv2.imread(image_path)
    
    # Create the Haar Cascade face detector
    face_cascade = cv2.CascadeClassifier(HARR_CASCADE_PATH)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=4)
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Resize the image for better display
    resized_image = cv2.resize(image, (800, 600))
    
    # Show the image with detected faces
    cv2.imshow("Detected Faces", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detect_faces_in_video():
    """
    Detect faces in video captured from the webcam and display the result in real-time.
    """
    # Open a connection to the webcam
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # Set the width of the frame
    cap.set(4, 480)  # Set the height of the frame

    # Create the Haar Cascade face detector
    face_cascade = cv2.CascadeClassifier(HARR_CASCADE_PATH)

    while True:
        # Capture frame-by-frame
        success, frame = cap.read()
        if not success:
            print("Failed to capture image.")
            break

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=4)

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Display the frame with detected faces
        cv2.imshow("Face Detection", frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

# Run face detection on a static image
detect_faces_in_image("path/to/your/image.jpg")  # Replace with the path to your image

# Run face detection on video from the webcam
detect_faces_in_video()
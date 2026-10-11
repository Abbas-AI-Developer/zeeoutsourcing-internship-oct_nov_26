import cv2

# Video open karo
cap = cv2.VideoCapture(r"D:\ZeeOutsourcing Internship\Computer Vision\abbas.mp4")

# Check karo video open hui ya nahi
if not cap.isOpened():
    print("Error: Video open nahi hui!")
    exit()

while True:

    # Video ka next frame read karo
    ret, frame = cap.read()

    # Agar frames khatam ho gaye
    if not ret:
        break

    # Har frame par green rectangle draw karo
    cv2.rectangle(
        frame,
        (50, 50),       # Top-left corner
        (350, 150),     # Bottom-right corner
        (0, 255, 0),    # Green color (BGR)
        2               # Border thickness
    )

    # Rectangle ke andar text likho
    cv2.putText(
        frame,
        "Hello Abbas",             # Text
        (60, 110),                  # Text position
        cv2.FONT_HERSHEY_SIMPLEX,   # Font
        1,                          # Font size
        (0, 255, 0),                # Green color
        2                           # Text thickness
    )

    # Processed frame show karo
    cv2.imshow("Video with Box and Text", frame)

    # Q press karne par video band
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

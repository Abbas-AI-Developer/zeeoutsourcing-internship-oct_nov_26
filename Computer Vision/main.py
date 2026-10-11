import cv2

img = cv2.imread(r"D:\ZeeOutsourcing Internship\Computer Vision\abbas.jpeg")

if img is not None:
    cv2.imshow("My First Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image nahi mili!")
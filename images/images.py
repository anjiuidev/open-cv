import cv2
# print(cv2.__version__)

img = cv2.imread('Koala.jpg', 0)

# print(img)

cv2.imshow("image", img)
key = cv2.waitKey(0)
# print(key)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite("KoalaCopy.jpg", img)
    cv2.destroyAllWindows()
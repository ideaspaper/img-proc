import cv2
import numpy as np

imcolor = cv2.imread('./images/lenna.png', cv2.IMREAD_COLOR)
imgray = cv2.imread('./images/lenna.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow(
    'Color -> Grayscale',
    np.hstack((
        imcolor,
        cv2.merge((imgray, imgray, imgray))
    ))
)

cv2.waitKey(0)
cv2.destroyAllWindows()

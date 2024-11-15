import cv2
import numpy as np


ROBINSON_MASK = [
    np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]]),  
    np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),  
    np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]),  
    np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]),  
    np.array([[2, -1, 0], [-1, 0, 1], [0, 1, -2]]),  
    np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]]),  
    np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]]),  
    np.array([[0, -1, -2], [1, 0, -1], [2, 1, 0]])   
]

def apply(image):
    height, width = image.shape
    edgeimg = np.zeros_like(image, dtype=np.uint8)

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            max_gradient = 0

            
            for mask in ROBINSON_MASK:
                region = image[y-1:y+2, x-1:x+2]
                gradient = np.sum(region * mask)
                max_gradient = max(max_gradient, abs(gradient))

            edgeimg[y, x] = min(255, max_gradient)

    return edgeimg

def process(paths):
    for path in paths:
        image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            print(f"Error: Could not read {path}")
            continue

        imagenew = apply(image)
        output = f"new{path}"
        cv2.imwrite(output, imagenew)
        print(f"Processed image saved as: {output}")

paths = ["image1.jpg"]
process(paths)

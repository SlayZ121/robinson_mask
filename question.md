# Applying the Robinson 8-Direction Mask to Grayscale Images

## Objective
To implement a program that applies the Robinson 8-direction edge detection mask to a set of five grayscale images. The program should process each image and output the results highlighting the edges detected in all eight directions.

## Problem Description
Edge detection is a crucial operation in image processing, enabling the identification of object boundaries within images. The Robinson 8-direction mask is a gradient operator used for edge detection that considers eight compass directions (N, NE, E, SE, S, SW, W, NW) to calculate the gradient magnitude.

For this assignment, you are required to:
1. Read five grayscale images as input.
2. Apply the Robinson 8-direction edge detection masks to each image.
3. Compute the gradient magnitude for each direction.
4. Combine the results to produce a final edge-detected image for each input.
5. Save and display the output images.

"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    color_distance = ((red - pixel.red)**2+(green - pixel.green)**2+(blue - pixel.blue)**2)**(1/2)
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red_pixels = []
    green_pixels = []
    blue_pixels = []
    for i in range(len(pixels)):
        # Get all the red values in the list of pixels
        red_pixels.append(pixels[i].red)
        # Get all the green values in the list of pixels
        green_pixels.append(pixels[i].green)
        # Get all the blue values in the list of pixels
        blue_pixels.append(pixels[i].blue)
    red_total = 0
    green_total = 0
    blue_total = 0
    red_avg = 0
    blue_avg = 0
    green_avg = 0
    for i in range(len(red_pixels)):
        # Calculate the average of red values
        red_total += red_pixels[i]
        red_avg = red_total // len(pixels)
    for i in range(len(green_pixels)):
        # Calculate the average of green values
        green_total += green_pixels[i]
        green_avg = green_total // len(pixels)
    for i in range(len(blue_pixels)):
        # Calculate the average of blue values
        blue_total += blue_pixels[i]
        blue_avg = blue_total // len(pixels)
    rgb = [red_avg, green_avg, blue_avg]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    # Assume the best pixel is the first one in the list of pixels
    best_pixel = pixels[0]
    avg = get_average(pixels)
    color_distance = get_pixel_dist(pixels[0], avg[0], avg[1], avg[2])
    smallest_distance = color_distance

    for i in range(len(pixels)):
        color_distance = get_pixel_dist(pixels[i], avg[0], avg[1], avg[2])
        # Get the pixel with the smallest distance from the average red, green, and blue values
        if color_distance < smallest_distance:
            smallest_distance = color_distance
            best_pixel = pixels[i]
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    # Write code to populate image and create the 'ghost' effect
    # Get all pixels in same (x,y) of a list of image objects
    for y in range(result.height):
        for x in range(result.width):
            pixels_lst = []
            for i in range(len(images)):
                pixels_lst.append(images[i].get_pixel(x, y))
                # Find the best pixel in the same (x,y)
            best1 = get_best_pixel(pixels_lst)
            result_pix = result.get_pixel(x, y)
            result_pix.red = best1.red
            result_pix.green = best1.green
            result_pix.blue = best1.blue
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()

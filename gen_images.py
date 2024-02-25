import os
import numpy as np
from PIL import Image, ImageColor
from py_fumen_py import decode as pydecode


colors = { 'T': '#9739a2ff', 'I': '#42afe1ff', 'L': '#f38927ff', 'J': '#1165b5ff', 'S': '#51b84dff', 'Z': '#eb4f65ff', 'O': '#f6d03cff', 'X': '#868686ff', '_': '#ffffff00' }

# Define the image dimensions and generate random data for each color channel
width = 10
height = 4
red_channel = np.zeros(shape=(height, width), dtype=np.uint8)
green_channel = np.zeros(shape=(height, width), dtype=np.uint8)
blue_channel = np.zeros(shape=(height, width), dtype=np.uint8)

# Generate random data for the alpha channel
alpha_channel = np.zeros(shape=(height, width), dtype=np.uint8)

# Stack the color channels and the alpha channel to form a 3D array
data = np.stack((red_channel, green_channel, blue_channel, alpha_channel), axis=-1)


with open('fumens.txt') as f:
    fumens = [s.strip() for s in f.readlines()]

for fumen in fumens:
    board = pydecode(fumen)[0].field.string().replace('\n', '')[:-10].rjust(40,'_')
    for row in range(4):
        for column in range(10):
            color = ImageColor.getcolor(colors[board[row*10 + column]], "RGBA")
            for i in range(4): data[row][column][i] = color[i]

    # print(data)



    # Convert the NumPy array to a PIL Image object
    img = Image.fromarray(data, 'RGBA')

    # Define the output filename and folder path
    filename = fumen + '.png'
    folder_path = './images/'

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Save the image to the specified folder
    img.save(os.path.join(folder_path, filename))

    # print(f'Color image saved successfully to: {os.path.join(folder_path, filename)}')

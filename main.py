from PIL import Image
import sys

ASCII = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

fileName = input("Enter image file name: ")

# load image
try:
  img = Image.open(fileName);
  print("Successfully loaded image!")
  print("Image size: " + str(img.width) + " x " + str(img.height))
except IOError:
  print("Error: Image not found")
  sys.exit(1)

inp = input("Would you like to shrink the image? (yes/no) ")
while (inp != "yes" and inp != "no"):
  inp = input("Please enter a valid input: ")
if (inp == "yes"):
  fact = int(input("By what factor? "))
elif(inp == "no"):
  fact = 1

img = img.resize((int(img.width / fact), int(img.height / fact)))

# create list of tuples
pixels = list(img.getdata())
tuples = []
for i in range(img.height):
  arr = []
  for j in range(img.width):
    arr.append(pixels[i * img.width + j])
  tuples.append(arr)

# create list of brightness
brightness = []
for i in range(len(tuples)):
  arr = []
  for j in range(len(tuples[i])):
    tuple = tuples[i][j]
    arr.append(int((tuple[0] + tuple[1] + tuple[2]) / 3))
  brightness.append(arr)

# create list of ascii characters
ascii = []
for i in range(len(brightness)):
  arr = []
  for j in range(len(brightness[i])):
    arr.append(ASCII[(int)(brightness[i][j] / 4)])
  ascii.append(arr)

asciiString = ""
for i in range(len(ascii)):
  for j in range(len(ascii[i])):
    asciiString += ascii[i][j]
  asciiString += "\n"

with open("ascii_image.txt", "w") as f:
  f.write(asciiString)
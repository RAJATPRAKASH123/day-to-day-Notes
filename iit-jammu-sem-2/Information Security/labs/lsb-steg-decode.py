from PIL import Image

image_path = "encoded.png"

# Read image
img = Image.open(image_path)
pixels = img.load()
width, height = img.size

# print(type(pixels[1,1]))
print(img.mode)
print("Image width: ",width," height: ",height)


binmessage = ''
for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y]
            
        # get lsb
        binmessage += str(r & 0b00000001)

endindex = binmessage.find("00000000")

binmessage = binmessage[:endindex]


finalmessage = ''

for i in range(0, len(binmessage),8):
    
    bits = binmessage[i:i+8]
    finalmessage += chr(int(bits, 2))
    
print("Decoded message: ",finalmessage)
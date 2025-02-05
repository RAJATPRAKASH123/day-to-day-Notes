from PIL import Image

image_path = "/media/anyamanaska/FE96AE6E96AE275D/MTech/2-sem/IS/IS-Lab/TT.png"
message = "Send me 1 plate of Masala Dosa"
output = "encoded.png"

# Read image
img = Image.open(image_path)
pixels = img.load()
width, height = img.size

# print(type(pixels[1,1]))
print(img.mode)
print("Image width: ",width," height: ",height)

binmessage = str()
# convert to bits
for c in message:
    
    ascii_value = ord(c)
    binary_value = bin(ascii_value)[2:]

    while len(binary_value) < 8:
        binary_value = '0' + binary_value
        
    binmessage += binary_value

finalmessage = binmessage + "01010101"


mi = 0
for y in range(height):
    for x in range(width):
        if mi < len(finalmessage):
            r, g, b = pixels[x, y]
            
            # clear lsb
            r = r & 0b11111110
            
            # set
            r = r | int(finalmessage[mi])
            
            # print(finalmessage[mi],int(finalmessage[mi]))
            
            mi += 1

            pixels[x, y] = (r, g, b)

        if mi >= len(finalmessage):
            break
    if mi >= len(finalmessage):
        break


img.save(output)
print("Message encoded and saved in ",output)

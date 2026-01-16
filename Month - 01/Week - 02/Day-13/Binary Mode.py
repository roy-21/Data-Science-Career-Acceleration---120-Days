'''
DEEP DIVE: 13.3 Micro-Challenge: Binary Mode
Goal: Read an image file. 
Deep Dive: Use mode 'rb'. Text modes decode bytes to String (UTF-8). 
Binary modes return raw bytes, essential for images/PDFs.
'''

# Reading an image file in binary mode

with open("photo.jpg", "rb") as f:
    image_bytes = f.read()

print(type(image_bytes))  # <class 'bytes'>
print(f"Read {len(image_bytes)} bytes from the image file.")

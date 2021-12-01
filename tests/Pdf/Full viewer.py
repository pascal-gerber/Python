from wand.image import Image
import os
 
pdf_file = "mypdf.pdf"
 
files = []
with(Image(filename=pdf_file, resolution = 500)) as conn: 
    for index, image in enumerate(conn.sequence):
        image_name = os.path.splitext(pdf_file)[0] + str(index + 1) + '.png'
        Image(image).save(filename = image_name)
        files.append(image_name)

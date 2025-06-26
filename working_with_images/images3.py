from PIL import Image
word = Image.open("C:\\avyan\\python\\working_with_images\\word_matrix.png").convert("RGBA")
mask = Image.open("C:\\avyan\\python\\working_with_images\\mask.png").convert("RGBA")
resized_mask = mask.resize((1015, 559))
word.putalpha(100)
resized_mask.putalpha(200)
word.paste(im=resized_mask, box=(0, 0), mask=resized_mask)
word.show()


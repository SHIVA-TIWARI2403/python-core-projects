from tkinter import Image, ImageFilter, ImageEnhance

# Photo open karo
img = Image.open(
    r"C:\Users\SHIVA TIWARI\OneDrive\Pictures\Camera imports\2026-08-23\43609.jpg"
)

# Image ka size set karo
img.thumbnail((800, 800))

# Smooth effect
smooth = img.filter(ImageFilter.SMOOTH_MORE)

# Sharp effect
cartoon = smooth.filter(ImageFilter.SHARPEN)

# Contrast improve
cartoon = ImageEnhance.Contrast(cartoon).enhance(1.3)

# Colors improve
cartoon = ImageEnhance.Color(cartoon).enhance(1.2)

# Image save karo
cartoon.save("python_recreated_photo.png")

# Image screen par dikhao
cartoon.show()

print("Image successfully created!")
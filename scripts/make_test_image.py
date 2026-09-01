from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB", (600, 300), color="white")
draw = ImageDraw.Draw(image)

# Load an actual font at a readable size, instead of the tiny default one.
# "arial.ttf" ships with Windows, so this should work directly for you.
font = ImageFont.truetype("arial.ttf", 24)

lines = [
    "REPUBLIC OF INDIA PASSPORT",
    "NAME: TEST USER",
    "PASSPORT NO P1234567",
    "DATE OF BIRTH 02/10/2007",
    "DATE OF EXPIRY 10/05/2030",
]

y_position = 20
for line in lines:
    draw.text((20, y_position), line, fill="black", font=font)
    y_position += 40

image.save("test_document.png")
print("Saved test_document.png")
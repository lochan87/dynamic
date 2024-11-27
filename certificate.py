from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

def create_certificate(name):
    # Open a certificate template
    template = Image.open("template.png")  # Your template file
    draw = ImageDraw.Draw(template)

    # Define font and size (ensure the font file is available)
    font = ImageFont.truetype("Pinyon_Script\PinyonScript-Regular.ttf", 164)
    text_color = (0, 0, 0)  # Black color

    # Add participant's name (adjust coordinates as needed)
    draw.text((520, 580), name, fill=text_color, font=font)

    # Save to BytesIO instead of file
    certificate_io = BytesIO()
    template.save(certificate_io, format="PNG")
    certificate_io.seek(0)  # Reset pointer for reading
    return certificate_io
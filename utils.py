from reportlab.pdfgen.canvas import Canvas

def get_ideal_font_size(canvas: Canvas, text, font="Helvetica", max_width=83, min_size=7, default_size=11):
    current_size = default_size
    text_width = canvas.stringWidth(text, fontName=font, fontSize=default_size)

    while text_width > max_width and current_size > min_size:
        current_size -= 1
        text_width = canvas.stringWidth(text, fontName=font, fontSize=current_size)

    return 0 if text_width > max_width else current_size


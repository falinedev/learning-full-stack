"""
Generates a personalized "shirtificate" PDF for a given name using the FPDF library.

Prompts the user for their name, overlays the text "[Name] took CS50" onto a template image,
and saves the result as 'shirtificate.pdf'.
"""

from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="portrait", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", size=25)
pdf.image("shirtificate.png", w=180, x=15, y=58.5)
text = f"{name} took CS50"
pdf.set_xy(0, 110)
pdf.set_text_color(255, 255, 255)
pdf.cell(pdf.w, 10, text, align="C")

pdf.output("shirtificate.pdf")

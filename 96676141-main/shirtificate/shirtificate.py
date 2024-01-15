from fpdf import FPDF

name = input("Name: ")
text = name + " took CS50"

pdf = FPDF()
pdf.set_auto_page_break(auto=False, margin=0)
pdf.add_page()
pdf.set_font("Arial", "B", size=50)
pdf.cell(0, 50, "CS50 Shirtificate", ln=True, align="C")
pdf.image("shirtificate.png", x=5, y=80, w=200)
pdf.set_font("Arial", "B", size=30)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 180, text, align="C")
pdf.output("shirtificate.pdf")

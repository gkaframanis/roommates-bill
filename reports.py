import webbrowser
from fpdf import FPDF
import os


class PdfReport:
    """
        Creates a Pdf file that contains data about the flatmates
        such as their names, their due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, bill, *roommates):
        # unit: using points (pt)
        pdf = FPDF(orientation="P", unit="pt", format="A4")

        # Add a new page
        pdf.add_page(orientation="P")

        # Add icon
        pdf.image(name="./files/house.png", w=30, h=30, type="png")

        # Add some text
        pdf.set_font(family="Times", size=24, style="B")
        # We write in cells | When w=0 it means it takes up the whole line. | ln=1 so the next cell will be added under this cell.
        pdf.cell(w=0, h=40, txt="The Bill of the Roommates", border=0, align="C", ln=1)
        pdf.cell(w=0, h=40, txt=f"Total Bill: {bill.amount} $", border=0, align="C", ln=1)

        # Change the font for the rest of the text.
        pdf.set_font(family="Times", size=14, style="B")
        # Starts from the left side of the cell by default.
        pdf.cell(w=250, h=25, txt=f"Period: {bill.period}", border=0, ln=1)
        for roommate in roommates:
            pdf.set_font(family="Times", size=12)
            pdf.cell(w=200, h=25, txt=f"{roommate.name} - {roommate.pays(bill, *roommates)} $", ln=1)

        # Change my current dir to files and output it in there.
        os.chdir("files")

        pdf.output(self.filename)
        # Open the pdf file automatically to the default web browser pdf viewer.
        webbrowser.open(f"file://{os.path.realpath(self.filename)}")



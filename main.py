import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
file_list = glob.glob("invoices/*.xlsx")
dfs = []

for filepath in file_list:
    pdf = FPDF(orientation='p', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()
    pdf.set_font(family='Times', size=16, style='b')

    filename = Path(filepath).stem
    filename_split = filename.split('-')

    invoice = f"Invoice # {filename_split[0]}"
    date = f"Date {filename_split[1]}"

    pdf.cell(w=10, h=10, txt=invoice, align='L')
    pdf.ln(10)
    pdf.cell(w=10, h=10, txt=date, align='L')
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    dfs.append(df)
    pdf.output(f"PDFs/{filename}.pdf")
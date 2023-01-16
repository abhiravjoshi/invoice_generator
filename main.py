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
    invoice, date = filename.split('-')

    invoice_str = f"Invoice # {invoice}"
    date_str = f"Date {date}"

    pdf.cell(w=50, h=8, txt=invoice_str, align='L', ln=1)
    # pdf.ln(10)
    pdf.cell(w=50, h=8, txt=date_str, align='L')

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    dfs.append(df)

    pdf.output(f"PDFs/{filename}.pdf")
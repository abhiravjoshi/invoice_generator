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
    pdf.cell(w=50, h=8, txt=date_str, align='L', ln=2)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    column_list = df.columns

    # Add header for table
    pdf.set_font(family='Times', size=10, style='b')
    pdf.set_text_color(80, 80, 80)
    widths = [30, 65, 35, 30, 30]
    for i, column in enumerate(column_list):
        column = column.replace('_', ' ')
        column = column.title()
        if i == len(column_list)-1:
            pdf.cell(w=widths[i], h=8, txt=column, border=1, ln=1)
        else:
            pdf.cell(w=widths[i], h=8, txt=column, border=1)

    # Add rows to table
    for index, row in df.iterrows():
        pdf.set_font(family='Times', size=10)
        pdf.set_text_color(80, 80, 80)
        for i, column in enumerate(column_list):
            if i == len(column_list) - 1:
                pdf.cell(w=widths[i], h=8,
                         txt=str(row[column_list[i]]), border=1, ln=1)
            else:
                pdf.cell(w=widths[i], h=8,
                         txt=str(row[column_list[i]]), border=1)

    # set total price row with sum of total_price
    for i in range(len(column_list)-1):
        pdf.cell(w=widths[i], h=8, txt='', border=1)
    x = df['total_price'].sum()
    pdf.cell(w=widths[i], h=8, txt=str(x), border=1, ln=1)
    pdf.ln(30)

    # do the totals summary at the end
    pdf.set_font(family='Times', size=15, style='b')
    total_p_str = f"The total price is {x}."
    pdf.cell(w=50, h=8, txt=total_p_str, align='L', ln=1)

    # PythonHow section
    pdf.cell(w=30, h=8, txt="PythonHow", align='L')
    pdf.image("pythonhow.png", w=10)







    pdf.output(f"PDFs/{filename}.pdf")
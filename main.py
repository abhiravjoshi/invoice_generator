import pandas as pd
import glob
from fpdf import FPDF

file_list = glob.glob("invoices/*.xlsx")
dfs = []

for filepath in file_list:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    dfs.append(df)
import pandas as pd
from file_to_excel import get_df
import os


def append(ROOT, df):
    # append df to root
    root_df = pd.read_excel(ROOT)
    combined_df = pd.concat([root_df, df], ignore_index=True)
    # save to ROOT excel
    combined_df.to_excel(ROOT, index=False)
    return "Successfully updated existing Excel."

ROOT = r"C:\Users\dlam01\OneDrive - FGF Brands Inc\Desktop\projects\invoiceExtractor\InvoiceDataExtractor\ROOT.xlsxx"
df = get_df(r"InvoiceDataExtractor\122 Stribling LP.pdf")


print(os.access(ROOT, os.W_OK))
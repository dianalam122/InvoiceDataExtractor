import os
import pandas as pd
from file_to_excel import get_df, make_excel

UPLOAD_FOLDER = r'C:\Users\dlam01\OneDrive - FGF Brands Inc\Desktop\projects\InvoiceDataExtractor\uploads'

def convert_files_to_excel():
    # Convert file in uploads to excel
    combined_df = pd.DataFrame(ignore_index=True)

    for file in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, file)
        df = get_df(file_path)
        combined_df = combined_df.append(df)
    # Make excel
    return make_excel(combined_df)


convert_files_to_excel()
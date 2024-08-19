import fitz
import pandas as pd

# Extract text from PDF in horizontal order
def sort_text(file):
    words = []
    pdf_doc = fitz.open(file)
    for page_num in range(min(2, len(file))):
        page = pdf_doc[page_num]
        # create a word_list 
        word_list = page.get_text("words")
        for word in word_list:
            words.append(word)

    # create and manipulate df for specific cols
    df = pd.DataFrame(words)
    df = df.iloc[:, [0, 1, 4]]
    df.columns= ['x0', 'y0', 'word']

    # round to alow lenience for slight y0 value differences
    df.y0 = df.y0.round()

    # group words by Y coordinate sort by X coordinate
    sorted_df = df.groupby('y0').apply(lambda x:x.sort_values('x0')).reset_index(drop=True)
    sorted_text = sorted_df.groupby('y0')['word'].apply(lambda x:' '.join(x)).values
    text = '\n'.join(sorted_text)
    return text

pdf = r"C:\Users\dlam01\OneDrive - FGF Brands Inc\Desktop\projects\invoiceExtractor\InvoiceDataExtractor\3000010605 -CPS 300-4198-613-AUG2024.pdf"

text = sort_text(pdf)

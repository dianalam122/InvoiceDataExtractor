import easyocr
import pandas as pd
import cv2

def cleanup_text(text):
    return "".join([c if ord(c) < 128 else "" for c in text]).strip()

def display_image(image, results):
    image_file = cv2.imread(image)
    for (bbox, text) in results:
        (tl, tr, br, bl) = bbox
        tl = (int(tl[0]), int(tl[1]))
        tr = (int(tr[0]), int(tr[1]))
        br = (int(br[0]), int(br[1]))
        bl = (int(bl[0]), int(bl[1]))
        text = cleanup_text(text)
        cv2.rectangle(image_file, tl, br, (0, 255, 0), 2)
        cv2.putText(image_file, text, (tl[0], tl[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    cv2.imshow("Image", image_file)
    cv2.waitKey(0)

# data_output = [
#     [
#         'cps_number',
#         'Location',
#         'kWh_month',
#         'kWh_day',
#         'days_on_bill',
#         'billing_date',
#         'service_end_date',
#         'service_start_date',
#     ]
# ]

def process_image(image_path):
    reader = easyocr.Reader(['en'], gpu=False)
    results = reader.readtext(image_path, paragraph=True, x_ths=0.3)
    # convert result to df
    df = pd.DataFrame(results, columns=['bbox', 'text'])
    df.drop(columns=['bbox'], inplace=True)
    text = '\n\n'.join(df['text'].tolist())

    # print(text)
    return text

    # need to regex invoice number !!!
    # data_output.append([
    #     invoice_number
    # ])

    # display_image(image_path, results)

# invoice_file = "invoices/sample.pdf"


# Convert the PDF to images and process the first page
# pages = convert_from_path(invoice_file, first_page=1, last_page=1)  # Only extract the first page
# first_page_image = 'first_page.jpg'
# pages[0].save(first_page_image, 'JPEG')
# process_image(first_page_image)
# os.remove(first_page_image)

# pages = convert_from_path(invoice_file, first_page=2, last_page=2)
# second_page_image = 'second_page.jpg'
# pages[1].save(second_page_image, 'JPEG')
# process_image(second_page_image)
# os.remove(second_page_image)
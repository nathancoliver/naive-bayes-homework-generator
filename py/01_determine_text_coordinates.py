from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
import os

import pandas as pd
import numpy as np

files = os.listdir('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Questions')

print(files)

text_string = []
x_corr = []
y_corr = []
file_name = []

for file in files:

    path = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Questions/' + file

    fp = open(path, 'rb')

    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = PDFPage.get_pages(fp)



    for page in pages:
        # print('Processing next page...')
        interpreter.process_page(page)
        layout = device.get_result()
        for lobj in layout:
            if isinstance(lobj, LTTextBox):
                x, y, text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
                x0, y0_orig, x1, y1_orig = lobj.bbox
                y0 = page.mediabox[3] - y1_orig
                y1 = page.mediabox[3] - y0_orig

                x_corr.append(x)
                y_corr.append(y1)
                text_string.append(text)
                file_name.append(file[0:14])
                # print('At %r is text: %s' % ((x, y), text))
            # print(y1_orig, y1)


df = pd.DataFrame({'text':text_string,'x_corr':x_corr,'y_corr':y_corr,'question_file':file_name})

path_new = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_coordinates.csv'

df.to_csv(path_new,index=False)

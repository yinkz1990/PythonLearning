import PyPDF2
import sys


pdf_list = sys.argv[1:]


def combine_pdf(Pdf_List):
    merger = PyPDF2.PdfMerger()
    for Pdf in Pdf_List:
        print(Pdf)
        merger.append(Pdf)
    merger.write('super.pdf')


combine_pdf(pdf_list)

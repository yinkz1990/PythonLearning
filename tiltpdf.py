import PyPDF2


with open('./Pdf/sample.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]
    page.rotate(90)
    writer = PyPDF2.PdfWriter()
    print(writer)
    writer.add_page(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)

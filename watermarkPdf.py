import PyPDF2


output = PyPDF2.PdfWriter()

with open('./watermarked.pdf', 'rb') as watermarked:
    watermark = PyPDF2.PdfReader(watermarked)
    with open('super.pdf', 'rb') as file:
        template = PyPDF2.PdfReader(file)
        for i in range(len(template.pages)):
            page = template.pages[i]
            page.merge_page(watermark.pages[0])
            output.add_page(page)

            with open('watermarked_output.pdf', 'wb') as file:
                output.write(file)

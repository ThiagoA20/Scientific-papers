from PyPDF2 import PdfFileReader, PdfFileWriter
from os.path import abspath

def txt_rob(content, pdf_paths):
    content.originalContent = ''

    def convert_pdf_to_string(pdf):
        pdf = PdfFileReader(pdf, strict=False)
        for page_num in range(pdf.numPages):
            pageObj = pdf.getPage(page_num)

            try:
                txt = pageObj.extractText()
                try:
                    dirt = open("dirt_content.txt", "r")
                except:
                    dirt = open("dirt_content.txt", "w")
                dirt.writelines(txt)
                dirt.close()
            except:
                pass
            else:
                content.originalContent += f"{txt}\n"

    for pdf in pdf_paths:
        convert_pdf_to_string(abspath(pdf))

    print(content.originalContent)

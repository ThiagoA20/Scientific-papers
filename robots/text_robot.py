#!/usr/bin/env python3
# -*- coding; utf-8 -*-

from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import time


def txt_rob(content, pdf_names):
    content.originalContent = ''

    os.system(f"java -cp cermine-impl-1.13-jar-with-dependencies.jar pl.edu.icm.cermine.ContentExtractor -path {os.getcwd() + '/content/originals'} -outputs 'text'")
    time.sleep(15)
    for file_name in pdf_names:
        full_file_path = f"{os.getcwd() + '/content/originals/' + file_name + '.cermtxt'}"
        with open(full_file_path, 'r') as f:
            for line in f.readlines():
                if len(line) != 2:
                    content.originalContent += line
                else:
                    pass

    def removeBlankLines(text):
        allLines = text.split('\n')
        pure_content = ""
        for i in allLines:
            pure_content += f"{i + ' '}"
        content.originalContent = pure_content

    removeBlankLines(content.originalContent)
    print(content.originalContent)

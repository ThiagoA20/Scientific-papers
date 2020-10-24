#!/usr/bin/env python3
# -*- coding; utf-8 -*-

from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import time
import re
from nltk.tokenize import sent_tokenize

"Catch data structure and a list with the names of the files as parameters"
def txt_rob(content, pdf_names):
    content.originalContent = ''

    "Extract text from articles calling java packages"
    os.system(f"java -cp cermine-impl-1.13-jar-with-dependencies.jar pl.edu.icm.cermine.ContentExtractor -path {os.getcwd() + '/content/originals'} -outputs 'text'")
    time.sleep(15)

    "Save extracted text from pdf's inside data structure as string"
    for file_name in pdf_names:
        full_file_path = f"{os.getcwd() + '/content/originals/' + file_name + '.cermtxt'}"
        with open(full_file_path, 'r') as f:
            for line in f.readlines():
                if len(line) != 2:
                    content.originalContent += line
                else:
                    pass

    "Clean the text for watson analisys"
    def cleaning_txt(text):

        def removeBlankLines(text):
            allLines = text.split('\n')
            pure_content = ""
            for i in allLines:
                pure_content += f"{i + ' '}"
            content.cleanContent = pure_content

        def removeReferences():
            pass

        def removeCopyright():
            content.cleanContent = content.cleanContent.replace('This article is protected by copyright. All rights reserved.', '')

        def removeLinks():
            content.cleanContent = re.sub(r'\(http.*?\)', "", content.cleanContent)

        def removeRodapeMarks():
            content.cleanContent = re.sub(r'\[[0-9]{1,2}-?\w*\]', "", content.cleanContent)

        removeBlankLines(text)
        removeReferences()
        removeCopyright()
        removeLinks()

    def making_scentences(text):

        content.Scentences.text = sent_tokenize(text)

    cleaning_txt(content.originalContent)
    making_scentences(content.cleanContent)
    print(content.Scentences.text)

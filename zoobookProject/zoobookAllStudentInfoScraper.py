from pdfminer.high_level import extract_text

year = 1991
f = open('fullZoobooks.txt', 'w')
while year < 2023:
    filename = "Zoobook_" + str(year) + ".pdf"
    f.write("----------" + str(year) + "----------")
    f.write("\n")
    f.write(extract_text(filename))
    f.write("\n")
    year += 1
f.close()

from PyPDF2 import PdfReader 
  
year = 1991
f = open('fullZoobooksPyPDF2.txt', 'w')
while year < 2023:
    filename = "Zoobook_" + str(year) + ".pdf"
    reader = PdfReader(filename) 
    f.write("----------" + str(year) + "----------")
    f.write("\n")
    for page in reader.pages:
        f.write(page.extract_text())
    f.write("\n")
    year += 1
f.close()

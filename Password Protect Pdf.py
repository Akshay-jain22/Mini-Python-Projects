from PyPDF2 import PdfFileReader, PdfFileWriter

def secure_pdf(file, password):
    parser = PdfFileWriter()
    pdf = PdfFileReader(file + '.pdf')
    
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    parser.encrypt(password)

    with open(f"{file}_encrypted.pdf", "wb") as f:
        parser.write(f)
        f.close()
    print(f'Encrypted File : {file}_encrypted.pdf Created')

if __name__ == "__main__":
    file = 'files/merged_pdf'
    password = 'AJ'
    secure_pdf(file, password)

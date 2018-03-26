from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger


def extract_from_pdf():
    pdf_file = input("PDF name: ") + '.pdf'
    start_page = input("Start page: ")
    end_page = input("End page: ")
    with PdfFileReader(pdf_file, 'rb') as pdf:
        pass



def merge_pdfs():
    print(__name__)


def main():
    menu = '1. Extract from PDF\n'
    menu += '2. Merge PDFs\n'
    menu += '0. Exit\n'

    option = -1
    while option is not '0':
        print(menu)
        option = input()
        if option is 1:
            extract_from_pdf()
        elif option is 2:
            merge_pdfs()

main()



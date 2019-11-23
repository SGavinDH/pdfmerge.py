# pdf_merging.py

from PyPDF3 import PdfFileReader, PdfFileWriter
from argparse import ArgumentParser as argparse_ArgumentParser

commands = argparse_ArgumentParser(description='merge pdf')
commands.add_argument('-a',    help='first pdf')
commands.add_argument('-b',    help='second pdf')
commands, unknown = commands.parse_known_args()

pdf1 = commands.a
pdf2 = commands.b

def merge_pdfs(paths, output):
	pdf_writer = PdfFileWriter()

	for path in paths:
		pdf_reader = PdfFileReader(path)
		for page in range(pdf_reader.getNumPages()):
			# Add each page to the writer object
			pdf_writer.addPage(pdf_reader.getPage(page))

	# Write out the merged PDF
	with open(output, 'wb') as out: 
		pdf_writer.write(out)

if __name__ == '__main__':
	paths = [pdf1, pdf2]
	merge_pdfs(paths, output='merged.pdf')

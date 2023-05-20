from zipfile import ZipFile

file_name = "provide your file name with .zip extension"

with ZipFile('winemag-data-130k-v2.csv.zip', 'r') as zip:
	zip.printdir()

	print('Extracting all the files now...')
	zip.extractall()
	print('Done!')

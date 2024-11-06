from __future__ import print_function
import sys
from os import makedirs, walk, listdir
from shutil import rmtree
from os.path import join, exists, abspath
from urllib.request import urlopen
from urllib.error import HTTPError
from PIL import Image
from fpdf import FPDF
from ast import literal_eval
from re import findall, sub
from pickle import dump, load

"""
Author: Michael Chung (mchung96@stanford.edu)

Download scores and parts from the NYPhil's Digital Archives!

To run, execute the command:

	python3 nyphil.py <url> <pathname>

<url> 		the URL of the archive page to be downloaded
			Make sure to cut off any URL variables (everything
	  		including and after the first "?"), OR put the URL
	  		in quotation marks
<pathname> 	the path to the root directory where you want the
  			files to be stored ("." for current folder)

Example valid command (this one downloads West Side Story!):

	python nyphil.py https://archives.nyphil.org/index.php/artifact/8c18b113-d77e-40df-a841-1e922b018cd8-0.1 .

NOTES:
1)	If you get an error that looks like this:
		socket.error: [Errno 54] Connection reset by peer
	Don't worry! Simply delete the last downloaded file (in
	case it got corrupted by the error), and run the exact
	same command as the first time to start it up again.
2)	Leave alone the file named 'info.txt'. It's generated
	by this script to keep track of some useful information
	to speed things up if something goes wrong the first
	time.
"""

instructions = '''
USAGE:
\tpython nyphil.py <url> <pathname>
where
\t<url>\t\tis the url of the page you want to download from
\t\t\t(everything before the first "?" - if there is one)
\t<pathname>\tis the path to the root folder for this download
\t\t\t("." for current folder)
'''

# Added to the end of each page URL. 2000 is the height in pixels
suffix = '.jp2/portrait/2000'
# Default values for (downloaded, rasterized, converted, cleaned)
default_progress = (False, False, False, False)
# Filename of progress log file
info_fname = 'info.txt'

'''
Downloads all pages of a given instrument part as JPG images
'''
def download_instrument(piece_root, instrument, prefix):
	print('=====%s=====' % instrument.upper())
	# Create the directory for the instrument if it doesn't already exist
	directory = join(piece_root, instrument)
	if not exists(directory):
		makedirs(directory)
	# Repeat until there are no more pages
	page_num = 1
	while True:
		# Sometimes the website is slow to respond, so we get an error. However, don't
		# stop trying unless it's actually a 404 (which means we're done)
		got_404 = False
		while not got_404:
			# Piece together the filename (of the new file we want to create),
			# along with its full path
			filename = '%s_%s.jpg' % (instrument, str(page_num).zfill(3))
			path_to_file = join(directory, filename)
			if exists(path_to_file):
				page_num += 1
				continue
			# Piece together the url to download
			page_url = prefix + str(page_num).zfill(3) + suffix
			try:
				# Try to open the url (this is where an error could happen)
				file = urlopen(page_url)
				print('Downloading %s...' % filename)
				# Only write the file if it doesn't already exist
				with open(path_to_file, 'wb') as new_page:
					new_page.write(file.read())
				page_num += 1
			except HTTPError as e:
				# If it's a 404, set the boolean to True (so we don't try again)
				if e.code == 404:
					got_404 = True
				# Otherwise, just print the error and try again
				else:
					print(e)
		if got_404:
			print('Done with %s!' % instrument)
			break

'''
Opens the source code of the 'View Part' page for each instrument
and retrieves the URL stub of each JPG file
'''
def get_url_stubs(urls):
	stubs = []
	for url in urls:
		try:
			webpage = str(urlopen(url).read())
			# Parse out the .jpg file
			stub = findall(r'src="([^"]+)\d{3}\.jp2/portrait/', webpage)[0]
			stubs.append(stub)
		except HTTPError as e:
			print(e)
	return stubs

'''
Reads through info.txt and retrieves pre-loaded data
'''
def get_preloaded_info(piece_root):
	filename = join(piece_root, info_fname)
	with open(filename, 'rb+') as f:
		url = load(f)
		composer = load(f)
		title = load(f)
		url_stubs = load(f)
		downloaded = False
		rasterized = False
		converted = False
		cleaned = False
		progress = (downloaded, rasterized, converted, cleaned)
		for i in range(4):
			try:
				progress[i] = load(f)
			except EOFError:
				break
		return composer, title, url_stubs, progress

'''
Opens the URL supplied by the user and parses out the following information:
- Name of composer
- Title of piece
- URL stubs for each instrument part
'''
def parse_webpage(url, root):
	print('\nParsing web page...', end='')
	sys.stdout.flush()
	try:
		webpage = str(urlopen(url).read())
		# Parse out the composer's name and the title of the piece
		lastname, firstname, title = findall(r'og:title" content="([^,]+),\s+([^/]+)/ ([^"]+)', webpage)[0]
		lastname = sub(r'\s+', ' ', lastname.strip())
		firstname = sub(r'\s+', ' ', firstname.strip())
		title = sub(r'\s+', ' ', title.strip())

		if exists(join(root, lastname, title)):
			preloaded_info = get_preloaded_info(join(root, lastname, title))
			print('already parsed! Using pre-loaded information.')
			return preloaded_info

		# Parse out all of the instruments
		instruments = findall(r'<!-- instrument -->[^>]+>([\w ]+)', webpage)
		instruments = [i.replace(' ', '_') for i in instruments]
		# Parse out the links to each instrument part
		part_urls = findall(r'href="([^"]+)">Explore Part', webpage)
		stubs = get_url_stubs(part_urls)
		# Tack the information for the full score onto the ends of the lists
		scorePart = findall(r'src="([^"]+)\d{3}\.jp2/portrait/[^\n]+\n+[^>]+>View Score', webpage)
		if len(scorePart) > 0:
			instruments.append('Score')
			stubs.append(findall(r'src="([^"]+)\d{3}\.jp2/portrait/[^\n]+\n+[^>]+>View Score', webpage)[0])
		if len(stubs) == 0 or len(instruments) != len(stubs):
			return None, None, None, default_progress
		url_stubs = zip(instruments, stubs)
		print('complete!')
		return lastname, title, url_stubs, default_progress
	except HTTPError as e:
		print(e)
		return None, None, None, default_progress

'''
Downloads every page of every instrument part
'''
def download_images(url_stubs, piece_root):
	print('\nBeginning downloads...')
	for instrument, prefix in sorted(url_stubs):
		download_instrument(piece_root, instrument, prefix)
	filename = join(piece_root, info_fname)
	with open(filename, 'ab') as f:
		dump(True, f)
	print('Finished downloads!')

'''
Loops through every image and creates a rasterized version
'''
def rasterize_images(piece_root):
	print('\nRasterizing images...')
	dirs = [x for x in listdir(piece_root) if not x.endswith('_rasterized')]
	for instrument in sorted(dirs):
		if instrument == '.DS_Store' or instrument == info_fname:
			continue
		print('%s...' % instrument)
		instrument_dir = join(piece_root, instrument)
		rasterized_dir = instrument_dir + '_rasterized'
		if not exists(rasterized_dir):
			makedirs(rasterized_dir)
		for page in sorted(listdir(instrument_dir)):
			img_path = join(instrument_dir, page)
			new_img_path = join(rasterized_dir, page)
			if page == '.DS_Store' or exists(new_img_path):
				continue
			color_image = Image.open(img_path)
			rasterized = color_image.convert('1', dither=Image.NONE)
			rasterized.save(new_img_path)
	filename = join(piece_root, info_fname)
	with open(filename, 'ab') as f:
		dump(True, f)

'''
Packages together each instrument's pages into a single PDF for
that instrument part
'''
def convert_images(piece_root):
	print('\nConverting rasterized images to PDFs...')
	rasterized_dirs = [x for x in listdir(piece_root) if x.endswith('_rasterized')]
	for instrument in sorted(rasterized_dirs):
		new_fname = '%s.pdf' % instrument[:instrument.find('_rasterized')]
		new_path = join(piece_root, new_fname)
		if instrument == '.DS_Store' or instrument == info_fname or exists(new_path):
			continue
		print('%s...' % instrument)
		instrument_dir = join(piece_root, instrument)
		new_pdf = FPDF('P', 'in', 'Letter')
		for page in sorted(listdir(instrument_dir)):
			if page == '.DS_Store':
				continue
			new_pdf.add_page()
			new_pdf.image(join(instrument_dir, page), 0, 0, 8.5, 11)
		new_pdf.output(new_path)
	filename = join(piece_root, info_fname)
	with open(filename, 'ab') as f:
		dump(True, f)

'''
Record parsed information in case of download failure
'''
def record_variables(piece_root, url, composer, title, url_stubs, progress):
	print('\nRecording variables for future use...')
	if not exists(piece_root):
		makedirs(piece_root)
	filename = join(piece_root, info_fname)
	print(filename)
	with open(filename, 'wb') as f:
		dump(url, f)
		dump(composer, f)
		dump(title, f)
		dump(url_stubs, f)

'''
Delete all unnecessary files, leaving only the final PDFs (and info.txt)
'''
def clean_up(piece_root):
	for f in listdir(piece_root):
		if f[-4] == '.':
			continue
		full_path = join(piece_root, f)
		rmtree(full_path)
	filename = join(piece_root, info_fname)
	with open(filename, 'ab') as f:
		dump(True, f)

def main():
	args = sys.argv[1:]
	if len(args) < 2:
		print(instructions)
		return

	url = args[0]
	root = abspath(args[1])

	composer, title, url_stubs, progress = parse_webpage(url, root)

	if url_stubs is None:
		print('Failed to parse the page.')
		return

	piece_root = join(root, composer, title)
	if not exists(join(piece_root, info_fname)):
		record_variables(piece_root, url, composer, title, url_stubs, progress)
	downloaded, rasterized, converted, cleaned = progress

	if not downloaded:
		download_images(url_stubs, piece_root)
	if not rasterized:
		rasterize_images(piece_root)
	if not converted:
		convert_images(piece_root)
	if not cleaned:
		clean_up(piece_root)

	print('\nComplete! Your files can be found in "%s".\n' % join(root, composer, title))

if __name__ == '__main__':
	main()

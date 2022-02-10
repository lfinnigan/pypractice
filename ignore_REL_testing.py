import unicodecsv as csv
from pymarc import MARCReader
from os import listdir
from re import search

# What I really want is for the script to iterate through all
# mrc files in a specified directory (fixtures). I tried using the
# 'Use case 1' here as a template, but wasn't successful:
# https://acrl.ala.org/techconnect/post/hacking-in-python-with-pymarc/
# Ideally, the script would allow me to assess or work with all of
# the files in the source directory at once, so it should either 
# combine the marc files themselves into one first, or iterate over
# all of the files separately and give me a combined result.



# change the source directory to whatever directory your .mrc files are in
SRC_DIR = 'fixtures'

# get a list of all .mrc files in source directory 
file_list = filter(lambda x: search('.mrc', x), listdir(SRC_DIR))

#create tab delimited text file that quotes if special characters are present
#csv_out = csv.writer(open('related_output.txt', 'wb'), delimiter = '\t', 
#quotechar = '"', quoting = csv.QUOTE_MINIMAL)

#create the header row
#csv_out.writerow(['mms'])

for item in file_list:
  fd = open(SRC_DIR + '/' + item, 'r')
  reader = MARCReader(fd)
  for record in reader:
        if (record['REL']):
            print(record['001'].value())
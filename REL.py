from pymarc import MARCReader

my_marc_file = 'fixtures/related-records__2021120821_26121776070003811_new_13_clean_rev.mrc_clean_rev.mrc'

#print MMS ID when MARC tag REL exists

with open(my_marc_file, 'rb') as fh:
    reader = MARCReader(fh, to_unicode=True, force_utf8=True)
    for record in reader:
        if (record['REL']):
            print(record['001'].value())
        else:
            pass
import shutil
import glob
from pymarc import MARCReader

# define source directory where marc files live
src_dir = 'fixtures/*'

# combine all marc files in source directory
with open('joined.mrc', 'wb') as joined:
    for i in glob.glob(src_dir):
    #this line takes every file in fixtures and iterates them through a loop
        with open(i, 'rb') as readfile:
            shutil.copyfileobj(readfile, joined)

# work magic on whatever is in the resulting joined file; here I would
# like for all records with 'REL' tag to write to related_filtered.mrc.
# right now only one record is being written to the file, but it should be 
# more than that (see commented out print function to see how many should be there. 

with open('joined.mrc', 'rb') as joined:
    reader = MARCReader(joined, to_unicode=True, force_utf8=True)
    for record in reader:
        if (record['REL']):
               # with open('related_filtered.mrc', 'wb') as out:
               #   out.write(record.as_marc())
               print(record['001'].value())
        else:
            pass

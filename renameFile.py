import os
import time
import pathlib
from uuid import uuid4

path = r"F:"
files = os.listdir(path)

for filename in files:
    file_extension = pathlib.Path(filename).suffix
    # dt = str(random.random())
    dt = time.strftime('%H%M%S')+ str(uuid4())
    # dt = datetime.datetime.now().strftime('%Y%M%D-%H%M%S')

    newname = 'VID-'+dt+file_extension

    if file_extension != '':
        oldpathname = os.path.join(path, filename)
        newpathname = os.path.join(path, newname)

        os.rename(oldpathname, newpathname)
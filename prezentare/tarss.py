
from zipfile import ZipFile
from tarfile import TarFile
import tarfile
from bz2 import BZ2File


pats = ['showsys.out', 'showsys_-d.out', 'showversion.out']
mapp = []
# with tarfile.open('prezentare.zip', 'r') as tf:
    # for i in tf:
    #     for j in pats:
    #         if i.name.endswith(j):
    #             infile = tf.extractfile(i)
    #             mapp.append((i.name, infile.readlines()))
with ZipFile('prezentare.zip', 'r') as zf:
    for i in zf.filelist:
        with tarfile.open(zf.extract(i)) as tf:
            for i in tf:
                for j in pats:
                    if i.name.endswith(j):
                        infile = tf.extractfile(i)
                        import ipdb
                        ipdb.set_trace()
                        mapp.append((i.name, infile.readlines()))

# mapp.append((1, 2))
# asd = [(1, 2),(1, 3),(1, 4)]

import ipdb
ipdb.set_trace()
print()


# raw_content.append(get_relevant_files_from_tar(j, patterns))
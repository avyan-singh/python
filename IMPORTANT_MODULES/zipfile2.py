import zipfile
zipobj=zipfile.ZipFile('compressed file.zip','r')
zipobj.extractall('extracted_content')
import shutil
path="C:\\avyan\\python\\extracted_content"
name='archived_file'
shutil.make_archive(name,'zip',path)
shutil.unpack_archive('archived_file.zip','unpacked_file','zip')
shutil.unpack_archive('unzip_me_for_instructions.zip','instructions','zip')

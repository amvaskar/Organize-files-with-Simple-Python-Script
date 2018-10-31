import os,shutil, datetime as dt
import sys
result_dict = {}

download_dir=sys.argv[1]
photos_extension = ("jpg", "JPEG", "jpeg","png","HEIC","svg","JPG") #add more file extension to be more accurate
videos_extension = ("mp4", "ovi")
scripts_extension = ("py","sh","txt","md")
book_extension = ("pdf","mobi","epub","PDF")
doc_extension = ("doc","docx","xlsx","csv","odt")
archive_extension = ("gz", "zip","deb")
pak_extension = ("pak")
for each in os.listdir(download_dir):
    if os.path.isfile(download_dir + each):
        file_src = str(download_dir+each)
        if file_src.endswith(photos_extension):
            result_dict.setdefault("Photos", []).append(each)
        if file_src.endswith(videos_extension):
            result_dict.setdefault("Videos",  []).append(each)
        if file_src.endswith(scripts_extension):
            result_dict.setdefault("Scripts",  []).append(each)
        if file_src.endswith(book_extension):
            result_dict.setdefault("Book", []).append(each)
        if file_src.endswith(doc_extension):
            result_dict.setdefault("Docs", []).append(each)
        if file_src.endswith(archive_extension):
            result_dict.setdefault("Archives", []).append(each)
        if file_src.endswith(pak_extension):
            result_dict.setdefault("PakFiles", []).append(each)
print(result_dict)

for key in result_dict:
    new_dir = download_dir+key+'/'
    os.makedirs(new_dir, exist_ok=True)
    [shutil.move(download_dir+each, new_dir+each) for each in result_dict[key]]
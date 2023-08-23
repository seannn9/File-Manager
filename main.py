import os
import pathlib
import shutil

dl_path = "Downloads\\"
pic_path = "Pictures\\"
dl = os.path.join(os.path.expanduser("~"), dl_path)
pic = os.path.join(os.path.expanduser("~"), pic_path)
for file in os.listdir(dl):
    if pathlib.Path(file).suffix == '.txt':
        shutil.move(dl+file, dl+'txt')
    elif pathlib.Path(file).suffix == '.pdf':
        shutil.move(dl+file, dl+'pdf')
    elif pathlib.Path(file).suffix == '.docx':
        shutil.move(dl+file, dl+'docx')
    elif pathlib.Path(file).suffix == '.jpg' or pathlib.Path(file).suffix == '.png':
        shutil.move(dl+file, pic)


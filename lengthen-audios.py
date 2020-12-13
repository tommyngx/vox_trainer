import random as rd
import os
import math
import soundfile as sf
import numpy as np

min_audio_length = 4 #second
# =========== PHAN LAY TEN FILES VA FOLDERS =============
dataset_path = "D:\\dataset-4s\\"

#Tai danh muc cac folder trong dataset_path
try:
    folder = os.listdir(dataset_path)
except IOError as e:
    print("Could not read dataset: " + str(e))
    exit(1)

#Lay ra danh sach cac files trong moi folder
file = []
for fol in folder:
    file.append(os.listdir(dataset_path + "\\" + fol))

# =============== PHAN XU LY IN TEN FILES =================

tobe_deleted_files = []

for fol in range(len(folder)): #Duyet tung folder 1
    for idx, val in enumerate(file[fol]): #Duyet tung file trong folder do
        #Xu ly file neu no < 4s
        data, samplerate = sf.read(dataset_path + folder[fol] + "\\" + val)
        channels = len(data.shape)
        length_s = len(data) / float(samplerate)
        if length_s >= min_audio_length:
            continue

        n = math.ceil(min_audio_length * samplerate / len(data))
        if channels == 2:
            data = np.tile(data, (n, 1))
        else:
            data = np.tile(data, n)
        sf.write(dataset_path + folder[fol] + "\\" + "new" + val, data, samplerate)

        tobe_deleted_files.append(dataset_path + folder[fol] + "\\" + val)

for f in tobe_deleted_files:
    # Xoa file cu di
    if os.path.exists(f):
        os.remove(f)
    else:
        print("The file does not exist")

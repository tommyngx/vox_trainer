import random as rd
import pandas as pd
import os

outputcsv = r"D:\\data-challenge\\pairs.csv"
outputtxt = "D:\\data-challenge\\test-list-4s-30.txt"
num_of_folders = 30 #Lay
# =========== PHAN LAY TEN FILES VA FOLDERS =============
# dataset_path = "D:\data-challenge\dataset"
dataset_path = "D:\dataset-4s\\"
#Folder dataset
try:
    folder = os.listdir(dataset_path)
except IOError as e:
    print("Could not read dataset: " + str(e))
    exit(1)

#Lay ra 30 folder cuoi cung (Hien tai thu tu chua duoc chuan)
for f in folder:
    # print("{0} len: {1}".format(f, len(f.split("-")[0])))
    if len(f.split("-")[0]) < 3:
        folder.remove(f)

for idx in range(len(folder) - 1, 0, -1):
    if len(folder[idx].split("-")[0]) < 3:
        folder.remove(folder[idx])
folder = folder[len(folder) - num_of_folders:len(folder)]

print("Danh sach folders: {0}".format(folder))
file = []
for fol in folder:
    file.append(os.listdir(dataset_path + "\\" + fol))

ftxt = open(outputtxt, "w")
# =============== PHAN XU LY GHEP CAP =================
count = 0
dataframe = []
for fol in range(len(folder)): #Duyet tung folder 1
    # print("files = {0}".format(file[fol]))
    for idx, val in enumerate(file[fol]): #Duyet tung file trong folder do
        #Thuc hien ghep doi voi cac cap giong nhau
        # print(""val)
        for i in range(idx, len(file[fol])):
            if val != file[fol][i]:
                count = count + 1
                #In ra pair 1
                #print("1 {0} - {1}".format(val, file[fol][i]))
                dataframe.append([1, "{0}/{1}".format(folder[fol], val), "{0}/{1}".format(folder[fol],file[fol][i])])
                ftxt.write("1 {0}/{1} {2}/{3}\n".format(folder[fol], val, folder[fol],file[fol][i]))

                # Chon ra folder ngau nhien khac folder hien tai
                randomfol = rd.randint(0, len(folder) - 1)
                while randomfol == fol:  # Neu folder chon ra trung voi folder hien tai
                    randomfol = rd.randint(0, len(folder) - 1)
                # Chon ra file ngau nhien trong folder vua chon
                randomfil = rd.randint(0, len(file[randomfol]) - 1)
                #In ra pair 0
                if rd.random() > 0.5:
                    #print("0 {0} - {1}".format(file[randomfol][randomfil], val))
                    dataframe.append([0, "{0}/{1}".format(folder[randomfol], file[randomfol][randomfil]), "{0}/{1}".format(folder[fol], val)])
                    ftxt.write("0 {0}/{1} {2}/{3}\n".format(folder[randomfol], file[randomfol][randomfil], folder[fol], val))
                else:
                    #print("0 {0} - {1}".format(file[randomfol][randomfil], file[fol][i]))
                    dataframe.append([0, "{0}/{1}".format(folder[randomfol], file[randomfol][randomfil]),
                                      "{0}/{1}".format(folder[fol], file[fol][i])])
                    ftxt.write("0 {0}/{1} {2}/{3}\n".format(folder[randomfol], file[randomfol][randomfil], folder[fol], file[fol][i]))
                    # dataframe.append([0, file[randomfol][randomfil], file[fol][i]])

print("Ta co {0} so cap cung folder".format(count))
ftxt.close()
#In ra file csv
df = pd.DataFrame(dataframe, columns=["label", "vid1", "vid2"])
df.to_csv(outputcsv, index = False, header=True)

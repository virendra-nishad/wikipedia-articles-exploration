#!/usr/bin/env python3

import pandas as pd


file_name = "finished-paths-back.csv"
df = pd.read_csv(file_name, header=None)

counter1 = [0]*12
diff = 0
total = 0
for ind in df.index:
    diff = int(df.loc[ind][0] - df.loc[ind][1])
    total += 1
    if diff > 10 :
        counter1[11] += 1
    else :
        counter1[diff] += 1

with open("percentage-paths-back.csv", "w") as writeFile:
    writeFile.write(str(round((counter1[0]/total)*100, 1))
    + "," + str(round((counter1[1]/total)*100, 1))
    + "," + str(round((counter1[2]/total)*100, 1))
    + "," + str(round((counter1[3]/total)*100, 1))
    + "," + str(round((counter1[4]/total)*100, 1))
    + "," + str(round((counter1[5]/total)*100, 1))
    + "," + str(round((counter1[6]/total)*100, 1))
    + "," + str(round((counter1[7]/total)*100, 1))
    + "," + str(round((counter1[8]/total)*100, 1))
    + "," + str(round((counter1[9]/total)*100, 1))
    + "," + str(round((counter1[10]/total)*100, 1))
    + "," + str(round((counter1[11]/total)*100, 1)) + "\n"
    )


file_name = "finished-paths-no-back.csv"
df = pd.read_csv(file_name, header=None)

counter1 = [0]*12

diff = 0
total = 0
for ind in df.index:
    diff = int(df.loc[ind][0] - df.loc[ind][1])
    total += 1
    if diff > 10 :
        counter1[11] += 1
    else :
        counter1[diff] += 1


with open("percentage-paths-no-back.csv", "w") as writeFile:
    writeFile.write(str(round((counter1[0]/total)*100, 1))
    + "," + str(round((counter1[1]/total)*100, 1))
    + "," + str(round((counter1[2]/total)*100, 1))
    + "," + str(round((counter1[3]/total)*100, 1))
    + "," + str(round((counter1[4]/total)*100, 1))
    + "," + str(round((counter1[5]/total)*100, 1))
    + "," + str(round((counter1[6]/total)*100, 1))
    + "," + str(round((counter1[7]/total)*100, 1))
    + "," + str(round((counter1[8]/total)*100, 1))
    + "," + str(round((counter1[9]/total)*100, 1))
    + "," + str(round((counter1[10]/total)*100, 1))
    + "," + str(round((counter1[11]/total)*100, 1)) + "\n"
    )
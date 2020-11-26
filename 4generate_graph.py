#!/usr/bin/env python3

import pandas as pd
import csv
import json
import numpy

#####################################
# NOTE have to sort the output data #
#####################################

file_name = "article-ids.csv"
df_categories = pd.read_csv(file_name, comment='#', skip_blank_lines=True, header=None)

article_ids_list = list(df_categories[:][1])

file1_r = open("src_data/shortest-path-distance-matrix.txt")
lines = file1_r.readlines()

zero_data_matrix = numpy.zeros(shape=(len(article_ids_list), len(article_ids_list)), dtype=int)



file_name = "edges.csv"
with open(file_name, 'w') as csvfile:
    counter = 0
    for line in lines:    
        if line[0] == '#' or line[0] == ' ' or line[0] == '\n':
            continue
        for i in range(len(line)-1):
            if line[i] == '1':
                csvfile.write(article_ids_list[counter] + "," + article_ids_list[i] + "\n")
                zero_data_matrix[counter][i] = 1
            else :
                if line[i] == '_' or line[i] == '0' :
                    zero_data_matrix[counter][i] = -1
                else :
                    zero_data_matrix[counter][i] = int(line[i])

        counter += 1

out_df = pd.DataFrame(data=zero_data_matrix, index=article_ids_list, columns=article_ids_list)
# for art in article_ids_list:
#     out_df[art] = out_df[art].apply(numpy.int64)
# print(out_df)
out_df.to_csv('distance_matrix.csv')
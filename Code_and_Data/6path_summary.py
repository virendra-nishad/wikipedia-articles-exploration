#!/usr/bin/env python3

import pandas as pd
import json
import csv


file_name = "src_data/paths_finished.tsv"
df = pd.read_csv(file_name, sep='\t', comment='#', skip_blank_lines=True, header=None)

file_name = "distance_matrix.csv"
distance_matrix_df = pd.read_csv(file_name, index_col=0)


file_name = "article_ids.json"
f = open(file_name)
article_ids_json = json.load(f)


articleids_list = list(article_ids_json.values())


paths = list(df.loc[ : , 3])

with open("finished-paths-no-back.csv", "w") as nobackFile, open("finished-paths-back.csv", "w") as backFile:
    for path in paths:
        back_list = [] # count back in path length
        noback_list = [] # does not count back in path length
        articles = path.split(';')
        for art in articles:
            if art == '<':
                back_list.append(art)
                if len(noback_list) > 0 :
                    noback_list.pop()
            else :
                back_list.append(art)
                noback_list.append(art)
        shortest_path = distance_matrix_df[article_ids_json[back_list[len(back_list)-1]]][article_ids_json[back_list[0]]]
        if shortest_path == -1 :
            continue
        
        nobackFile.write(str(len(noback_list)-1) + "," + str(shortest_path) + "," + str(round((len(noback_list)-1)/shortest_path, 1)) + "\n")
        backFile.write(str(len(back_list)-1) + "," + str(shortest_path) + "," + str(round((len(back_list)-1)/shortest_path, 1)) + "\n")
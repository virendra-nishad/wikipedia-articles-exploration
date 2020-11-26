#!/usr/bin/env python3

import pandas as pd
import json
import csv


#####################################################################
# Need to have only id in output file
# Please confirm it
#####################################################################



file_name = "src_data/articles.tsv"
df = pd.read_csv(file_name, sep='\t', comment='#', skip_blank_lines=True, header=None)

df["ids"] = "null"

# print(df)

articlename_id = {}

count = 1
for ind in df.index:
    number_str = str(count)
    number_str = number_str.zfill(4)
    number_str = "A" + number_str
    df.at[ind, "ids"] = number_str
    count += 1
    articlename_id[df.loc[ind][0]] = df.loc[ind]["ids"]

# print(df)
# print(articlename_id)

df.to_csv('article-ids.csv', header=False, index=False)

with open("article_ids.json", "w") as outfile:  
    json.dump(articlename_id, outfile, indent=4) 
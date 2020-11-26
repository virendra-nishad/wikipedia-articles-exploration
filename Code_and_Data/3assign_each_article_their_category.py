#!/usr/bin/env python3

import pandas as pd
import csv
import json

json_file = open("article_ids.json")
article_ids = json.load(json_file)

json_file = open("category_ids.json")
category_ids = json.load(json_file)

# print(article_ids)
# print()
# print(category_ids)

# file_name = "src_data/articles.tsv"
# df_article = pd.read_csv(file_name, sep='\t', comment='#', skip_blank_lines=True, header=None)

file_name = "src_data/categories.tsv"
df_categories = pd.read_csv(file_name, sep='\t', comment='#', skip_blank_lines=True, header=None)

df_categories["Article_ID"] = ""
df_categories["Category_ID"] = ""

# print(df_categories)

for ind in df_categories.index:
    df_categories.loc[ind, "Article_ID"] = article_ids[df_categories.loc[ind][0]]
    df_categories.loc[ind, "Category_ID"] = category_ids[df_categories.loc[ind][1]]

# for ind in df_categories.index:
#     print(df_categories.loc[ind]["Article_ID"], df_categories.loc[ind]["Category_ID"])

df_categories = df_categories.drop(df_categories.columns[0], axis=1)
df_categories = df_categories.drop(df_categories.columns[0], axis=1)

df_categories = df_categories.sort_values(df_categories.columns[0])
# print(df_categories)

df_categories.to_csv('article-categories.csv', header=False, index=False)
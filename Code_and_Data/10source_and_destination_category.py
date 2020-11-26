#!/usr/bin/env python3

import pandas as pd
import json

###########################################################################

file_name = "article_ids.json"
f = open(file_name)
article_ids_json = json.load(f) #########################

file_name = "article-categories.csv"
article_categories_df = pd.read_csv(file_name, header=None)
# print(article_categories_df)

articleids_list = article_ids_json.values()  #########################
articlenames_list = article_ids_json.keys()  #########################


articleid_categoryidlist_dict = {}
for id in articleids_list :
    articleid_categoryidlist_dict[id] = []

# A given article can be in many categories, find out all those categories the given article belong to
for ind in article_categories_df.index :
    articleid_categoryidlist_dict[article_categories_df.loc[ind][0]].append(article_categories_df.loc[ind][1])


file_name = "category-ids.csv"
category_ids = pd.read_csv(file_name, header=None)
category_list = list(category_ids.loc[:, 1])    #########################

catID_name_dict = {}  #########################
name_catID_dict = {}  #########################
for ind in category_ids.index :
    catID_name_dict[category_ids.loc[ind][1]] = category_ids.loc[ind][0]
    name_catID_dict[category_ids.loc[ind][0]] = category_ids.loc[ind][1]
###########################################################################

file_name = "src_data/paths_unfinished.tsv"
paths_unfinished_df = pd.read_csv(file_name, sep='\t', comment='#', skip_blank_lines=True, header=None)
file_name = "src_data/paths_finished.tsv"
paths_finished_df = pd.read_csv(file_name, sep='\t', comment='#', skip_blank_lines=True, header=None)

unfinished_count = {} #########################
finished_count = {} #########################


for ind in paths_unfinished_df.index :
    path = paths_unfinished_df.loc[ind][3]
    path_split = path.split(';')

    source_art_name = path_split[0]
    destination_art_name = paths_unfinished_df.loc[ind][4]
    source_cat_list = []
    destination_cat_list = []

    if source_art_name in articlenames_list :
        source_cat_list = articleid_categoryidlist_dict[article_ids_json[source_art_name]]
    else :
        continue
    if destination_art_name in articlenames_list :
        destination_cat_list = articleid_categoryidlist_dict[article_ids_json[destination_art_name]]
    else :
        continue
    if len(source_cat_list) == 0 or len(destination_cat_list) == 0 :
        continue

    for src in source_cat_list :
        for dst in destination_cat_list :
            # ignore path from category to itself
            src_cat_name = catID_name_dict[src]
            dst_cat_name = catID_name_dict[dst]
            
            src_cat_name_split = src_cat_name.split('.')
            dst_cat_name_split = dst_cat_name.split('.')
            src_name = src_cat_name_split[0]
            dst_name = dst_cat_name_split[0]
            # if src_name == dst_name :
            #     continue
            inskey = name_catID_dict[src_name] + "|" + name_catID_dict[dst_name]
            if inskey in unfinished_count.keys() :
                unfinished_count[inskey] += 1
            else :
                unfinished_count[inskey] = 1
            for i1 in range(1, len(src_cat_name_split)) :
                src_name = src_name + "." + src_cat_name_split[i1]
                for i2 in range(1, len(dst_cat_name_split)) :
                    dst_name = dst_name + "." + dst_cat_name_split[i2]
                    if src_name == dst_name :
                        continue
                    if src_name in name_catID_dict.keys() and dst_name in name_catID_dict.keys() :
                        inskey = name_catID_dict[src_name] + "|" + name_catID_dict[dst_name]
                    else :
                        continue
                    if inskey in unfinished_count.keys() :
                        unfinished_count[inskey] += 1
                    else :
                        unfinished_count[inskey] = 1



for ind in paths_finished_df.index :
    path = paths_finished_df.loc[ind][3]
    path_split = path.split(';')

    source_art_name = path_split[0]
    destination_art_name = path_split[-1]
    source_cat_list = []
    destination_cat_list = []

    if source_art_name in articlenames_list :
        source_cat_list = articleid_categoryidlist_dict[article_ids_json[source_art_name]]
    else :
        continue
    if destination_art_name in articlenames_list :
        destination_cat_list = articleid_categoryidlist_dict[article_ids_json[destination_art_name]]
    else :
        continue
    if len(source_cat_list) == 0 or len(destination_cat_list) == 0 :
        continue

    for src in source_cat_list :
        for dst in destination_cat_list :
            # ignore path from category to itself
            src_cat_name = catID_name_dict[src]
            dst_cat_name = catID_name_dict[dst]
            
            src_cat_name_split = src_cat_name.split('.')
            dst_cat_name_split = dst_cat_name.split('.')
            src_name = src_cat_name_split[0]
            dst_name = dst_cat_name_split[0]
            # if src_name == dst_name :
            #     continue
            inskey = name_catID_dict[src_name] + "|" + name_catID_dict[dst_name]
            if inskey in finished_count.keys() :
                finished_count[inskey] += 1
            else :
                finished_count[inskey] = 1
            for i1 in range(1, len(src_cat_name_split)) :
                src_name = src_name + "." + src_cat_name_split[i1]
                for i2 in range(1, len(dst_cat_name_split)) :
                    dst_name = dst_name + "." + dst_cat_name_split[i2]
                    if src_name == dst_name :
                        continue
                    if src_name in name_catID_dict.keys() and dst_name in name_catID_dict.keys() :
                        inskey = name_catID_dict[src_name] + "|" + name_catID_dict[dst_name]
                    else :
                        continue
                    if inskey in finished_count.keys() :
                        finished_count[inskey] += 1
                    else :
                        finished_count[inskey] = 1
# count = 0
# for key in finished_count.keys() :
#     print(key, finished_count[key])
#     count += 1
#     if count == 5 :
#         break

# print()
# print()
# count = 0
# for key in unfinished_count.keys() :
#     print(key, unfinished_count[key])
#     count += 1
#     if count == 5 :
#         break

key_set = set()
for key in finished_count.keys() :
    key_set.add(key)
for key in unfinished_count.keys() :
    key_set.add(key)
key_list = list(key_set)
# print(key_list)

with open("category-pairs.csv", "w") as writeFile :
    for key in key_list :
        cat_split = key.split('|')
        src = cat_split[0]
        dst = cat_split[1]
        fin_count = 0
        unfin_count = 0
        total = 0
        if key in finished_count.keys() :
            fin_count = finished_count[key]
            total += fin_count
        if key in unfinished_count.keys() :
            unfin_count = unfinished_count[key]
            total += unfin_count
        if total > 0 :
            fin_percent = round((fin_count/total)*100, 1)
            unfin_percent = round(100 - fin_percent, 1)
            writeFile.write(src + "," + dst + "," + str(fin_percent) + "," + str(unfin_percent) + "\n")
#!/usr/bin/env python3

import pandas as pd
import json


file_name = "src_data/paths_finished.tsv"
df = pd.read_csv(file_name, sep='\t', comment='#', skip_blank_lines=True, header=None)


path_list = list(df.loc[: , 3])


path_list_noback = []
src_dst_set = set()

for path in path_list :
    temp = path.split(';')
    if '<' in temp :
        continue
    path_list_noback.append(path)
    src_dst_set.add(str(temp[0] + "|" + temp[-1]))
    # print(temp[0]+"|"+temp[-1], path)

src_dst_path_list_dict = {}
for srcdst in src_dst_set :
    src_dst_path_list_dict[srcdst] = []

# src_dst_path_list_dict contains all path from src|dst
for path in path_list_noback :
    temp = path.split(';')
    src_dst_path_list_dict[temp[0] + "|" + temp[-1]].append(path)

# for key in src_dst_path_list_dict.keys() :
#     print(key, len(src_dst_path_list_dict[key]))

file_name = "article_ids.json"
f = open(file_name)
article_ids_json = json.load(f)
# print(article_ids_json)

file_name = "article-categories.csv"
article_categories_df = pd.read_csv(file_name, header=None)
# print(article_categories_df)

articleids_list = article_ids_json.values()


articleid_categoryidlist_dict = {}
for id in articleids_list :
    articleid_categoryidlist_dict[id] = []

# A given article can be in many categories, find out all those categories the given article belong to
for ind in article_categories_df.index :
    articleid_categoryidlist_dict[article_categories_df.loc[ind][0]].append(article_categories_df.loc[ind][1])


file_name = "category-ids.csv"
category_ids = pd.read_csv(file_name, header=None)
category_list = list(category_ids.loc[:, 1])

###########################################################################
catID_name_dict = {}
name_catID_dict = {}
for ind in category_ids.index :
    catID_name_dict[category_ids.loc[ind][1]] = category_ids.loc[ind][0]
    name_catID_dict[category_ids.loc[ind][0]] = category_ids.loc[ind][1]
###########################################################################

category_path_count_dict_nor = {}
category_occc_count_dict_nor = {}
category_path_count_dict_sml = {}
category_occc_count_dict_sml = {}
for cat in category_list :
    category_occc_count_dict_nor[cat] = 0
    category_path_count_dict_nor[cat] = 0
    category_occc_count_dict_sml[cat] = 0
    category_path_count_dict_sml[cat] = 0

for srcdst in src_dst_path_list_dict.keys() :
    paths = src_dst_path_list_dict[srcdst]
    smallest_path = paths[0]
    for path in paths :
        if len(smallest_path) > len(paths) :
            smallest_path = path

    articles_in_path = smallest_path.split(";")
    # for preparing dictionary of count
    category_in_path_set = set()
    for art in articles_in_path :
        cat_list = articleid_categoryidlist_dict[article_ids_json[art]]
        for cat in cat_list :
            category_in_path_set.add(cat)
    # cat dict key conatains all category ID encountered and it's value contains occurances
    cat_dict = {}
    for cat in category_in_path_set :
        cat_dict[cat] = 0   # initialize to 0
    for art in articles_in_path :
        cat_list = articleid_categoryidlist_dict[article_ids_json[art]]
        for cat in cat_list :
            cat_dict[cat] += 1  # update occurances
##################################################################################    
    for key in cat_dict.keys() :

        cat_name = catID_name_dict[key]
        cat_name_split = cat_name.split('.')
        # print(cat_name_split)
        name = cat_name_split[0]
        category_path_count_dict_sml[name_catID_dict[name]] += 1
        category_occc_count_dict_sml[name_catID_dict[name]] += cat_dict[key]
        for i in range(1, len(cat_name_split)) :
            name = name + "." + cat_name_split[i]
            category_path_count_dict_sml[key] += 1
            category_occc_count_dict_sml[key] += cat_dict[key]
##################################################################################                
    
    for path in paths :

        articles_in_path = path.split(";")
        category_in_path_set = set()
        for art in articles_in_path :
            cat_list = articleid_categoryidlist_dict[article_ids_json[art]]
            for cat in cat_list :
                category_in_path_set.add(cat)

        cat_dict = {}

        for cat in category_in_path_set :
            cat_dict[cat] = 0
        for art in articles_in_path :
            cat_list = articleid_categoryidlist_dict[article_ids_json[art]]
            for cat in cat_list :
                cat_dict[cat] += 1

        for key in cat_dict.keys() :

            cat_name = catID_name_dict[key]
            cat_name_split = cat_name.split('.')
            # print(cat_name_split)
            name = cat_name_split[0]
            category_path_count_dict_nor[name_catID_dict[name]] += 1
            category_occc_count_dict_nor[name_catID_dict[name]] += cat_dict[key]
            for i in range(1, len(cat_name_split)) :
                name = name + "." + cat_name_split[i]
                category_path_count_dict_nor[key] += 1
                category_occc_count_dict_nor[key] += cat_dict[key]

            # category_path_count_dict_nor[key] += 1
            # category_occc_count_dict_nor[key] += cat_dict[key]

with open("category-subtree-paths.csv", "w") as writeFile :
    for key in category_path_count_dict_sml.keys() :
        writeFile.write(key + "," + str(category_path_count_dict_nor[key])
        + "," + str(category_occc_count_dict_nor[key])
        + "," + str(category_path_count_dict_sml[key])
        + "," + str(category_occc_count_dict_sml[key]) + "\n")
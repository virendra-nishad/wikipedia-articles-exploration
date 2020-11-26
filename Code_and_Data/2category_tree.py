#!/usr/bin/env python3

import pandas as pd
import json
import csv


#####################################################################
# NOTE:
# There was one specefic issue that there was different level 
# with same key like Subject.Art.Art
# To overcome above issue I have appended level to make them unique
# Above will become Subject|0.Art|1.Art|2
# Hence can be easily implemented in BFS also
#####################################################################

# Correction
# Have to consider sorting length i.e 
# Subject.Art.Art
# Subject.Art.Artist
#
# or
#
# Subject.Art.Artist
# Subject.Art.Art

#####################################################################
def dfs(tree, root, counter, visited):
    q = []

    adding_first_node_to_q = str(root)
    q.append(adding_first_node_to_q)

    categories_id_dict = {}

    while len(q) > 0:
        front = q.pop(0)

        # Below code will use to prepare ID of form CXXXX
        temp_id = str(counter)
        temp_id = temp_id.zfill(4)
        temp_id = "C" + temp_id
        categories_id_dict[front] = temp_id
        counter += 1

        # We need a split here bcoz we are saving node from root to current node as node key
        # That is we are building back tree from heierchy tree, below are few examples of heierchy
        # Subject.Art
        # Subject.Art.Art
        # Subject.Art.Artist
        # So we are provided node details in cumulative form i.e from root to current node
        temp2 = front.split('.')
        # prefix = temp2[0]
        # for i in range(1, len(temp2)-1):
        #     prefix = prefix + "." str(temp2)
        suffix = temp2[len(temp2)-1]

        if suffix in tree.keys():
            for adj in tree[suffix]:
                q.append(str(front) + "." + str(adj))

    return categories_id_dict


#####################################################################


file_name = "src_data/categories.tsv"
df = pd.read_csv(file_name, sep='\t', comment='#', skip_blank_lines=True, header=None)

# print(df)


# Below set will contain all nodes of the tree
# leaf node will have empty children list
categories_set = set()

for ind in df.index:
    temp_str = df.iloc[ind][1]
    temp_list = temp_str.split('.')
    for i in range(len(temp_list)):
        categories_set.add(str(temp_list[i]+'|'+str(i)))


# initialize empty graph
# children will be updated in later part of code
# children might repeat so use set for initial phase
# later we will convert them to list and sort them
# In this graph there will be an edge from parent to it's child node

child_graph = {}
for cat in categories_set:
    child_graph[cat] = set()

for ind in df.index:
    temp_str = df.iloc[ind][1]
    temp_list = temp_str.split('.')
    for i in range(1, len(temp_list)):
        child_graph[temp_list[i-1]+'|'+str(i-1)].add(temp_list[i]+'|'+str(i))

# for key in child_graph.keys():
#     if len(child_graph[key]) == 0:
#         print(key, ": {NULL}")    
#     else :
#         print(key, " : ", child_graph[key])
#     print()


####################################################

# below is a tree with it's children in sorted order
tree = {}
for key in child_graph.keys():
    temp1_list = list(child_graph[key])
    temp1_list.sort()
    #temp1_list.sort(key=len, reverse=True)
    tree[key] = temp1_list

# for key in tree.keys():
#     print(key, " : ", tree[key])

####################################################

# subject
visited = {}
for key in tree.keys():
    visited[key] = 0

# for key in visited.keys():
#     print(key, visited[key])

# Below dict need to be revert back to original form as each nodes are appended with their level 
# Separated by '|'
categorypluslevel_Cid_dict = dfs(tree, "subject|0", 1, visited)

# print(categorypluslevel_Cid_dict)

category_id_dict = {}
for key in categorypluslevel_Cid_dict.keys():
    temp1_list = key.split('.')
    ki = temp1_list[0].split('|')[0]
    for i in range(1, len(temp1_list)):
        ki = ki + '.' + temp1_list[i].split('|')[0]
    category_id_dict[ki] = categorypluslevel_Cid_dict[key]

# for key in category_id_dict.keys():
#     print(key, category_id_dict[key])



with open('category-ids.csv', 'w') as csvfile: 
    for key in category_id_dict.keys():
        csvfile.write("%s,%s\n"%(key, category_id_dict[key]))

####################################################
# print(df)
# print(articlename_id)

# df.to_csv('article-ids.csv', header=False, index=False)

with open("category_ids.json", "w") as outfile:  
    json.dump(category_id_dict, outfile, indent=4) 
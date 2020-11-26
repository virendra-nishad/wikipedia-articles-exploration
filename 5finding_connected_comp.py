#!/usr/bin/env python3

import pandas as pd
import csv
import json
import sys

sys.setrecursionlimit(10**6)


def bfs(node, graph, seen):
    component = []
    q = []
    q.append(node)
    seen[node] = 1
    component.append(node)
    while len(q) > 0:
        front = q.pop(0)
        for adj in graph[front]:
            if seen[adj] == 1:
                continue
            q.append(adj)
            seen[adj] = 1
            component.append(adj)
    return component


def depth(graph, seen, cur_node, cur_level):
    seen[cur_node] = 1
    
    local_mx_node = cur_node
    local_mx_level = cur_level

    for adj in graph[cur_node]:
        if adj in seen.keys():
            if seen[adj] == 1:
                continue
            rec_mx_node, rec_mx_level = depth(graph, seen, adj, cur_level+1)
            if rec_mx_level > local_mx_level:
                local_mx_level = rec_mx_level
                local_mx_node = rec_mx_node
    return (local_mx_node, local_mx_level)


file_name = "article-ids.csv"
df_categories = pd.read_csv(file_name, comment='#', skip_blank_lines=True, header=None)

article_ids_list = list(df_categories[:][1])

graph = {}
for art in article_ids_list:
    graph[art] = []

file_name = "edges.csv"
df_edges = pd.read_csv(file_name, comment='#', skip_blank_lines=True, header=None)

for ind in df_edges.index:
    # print(df_edges.loc[ind][0], df_edges.loc[ind][1])
    graph[df_edges.loc[ind][0]].append(df_edges.loc[ind][1])

seen = {}
for item in article_ids_list:
    seen[item] = 0

with open("graph-components.csv", 'w') as outFile:
    for item in article_ids_list:
        if seen[item] == 1:
            continue
        comp = bfs(item, graph, seen)
        
        sub_seen = {}
        for item1 in comp:
            sub_seen[item1] = 0
    
        
        end_node1, dist1 = depth(graph, sub_seen, comp[0], 0)
        
        for key in sub_seen.keys():
            sub_seen[key] = 0
        
        end_node2, dist2 = depth(graph, sub_seen, end_node1, 0)
        
        diameter = dist2
        numberofnodes = len(comp)
        numberofedges = 0
        for item in comp:
            numberofedges += len(graph[item])
        outFile.write(str(numberofnodes) + "," + str(numberofedges) + "," + str(diameter) + "\n")

    
file_name = "graph-components.csv"
df = pd.read_csv(file_name, header=None)
df = df.sort_values(df.columns[0])
df.to_csv('graph-components.csv', header=False, index=False)

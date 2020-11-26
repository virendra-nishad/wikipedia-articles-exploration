# python code descriptions

## run.sh
* This script will run the entire project

## 1article_to_id.py
* Augment the names of the articles in articles.tsv in the order given to have ids rom A0001 to A4604.
* output : article-ids.csv

## 2category_tree.py
* Convert the categories of the articles from categories.tsv into a hierarchy.Starting from subject, assign them ids starting from C0001 till the end. Used breadth-first ordering with the children ordered in alphabetical order.
* output : category-ids.csv.

## 3assign_each_article_their_category.py
* Augment the article-ids.csv file to include all the categories the corresponding article is in. If an article has no category
* output : article-categories.csv

## 4generate_graph.py
* construct the directed graph of articles in an edge adjacency list format.
* output : edges.csv

## 5finding_connected_comp.py
* Find connected components in the graph
* output : graph-components.csv

## 6path_summary.py
* For every finished paths by human. Followings are observed
	1. Length of path traversed by human
	2. Length of shortest path
	3. Ratio of human path to shortest path
* outputs - one that does not count the back clicks, and the one that does : finished-paths-no-back.csv and finished-paths-back.csv

## 7path_summary2.py
* For above files, prepared percentage of human paths that have:
	1. Exactly the same path length as the shortest path
	2. Path length is 1 to 10 more than the shortest path
	3. Path length is 11 or more than the shortest path
* output : percentage-paths-no-back.csv and percentage-paths-back.csv

## 8category_summary.py
* For each finished human path (without back links) and its corresponding shortest path,the following for each category are observed
	1. Number of paths this category is traversed.
	2. Number of times this category is traversed
* output : category-paths.csv

## 9category_summary2.py
* Above is repeated by considering the counts of categories under a category’s subtree as its counts as well.
* output : category-subtree-paths.csv

## 10source_and_destination_category.py
* For every unfinished path in paths unfinished.tsv, the source and destination category pair were found taking into account all the sub-categories under it.
* Same are repeated for every finished path.
* For every source-destination category pair, the percentage of finished and unfinished paths were explored.
* output : category-pairs.csv

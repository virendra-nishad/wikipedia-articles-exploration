#!/bin/sh
	
echo "started ..."

cd Code_and_Data

python3 1article_to_id.py
python3 2category_tree.py
python3 3assign_each_article_their_category.py
python3 4generate_graph.py
python3 5finding_connected_comp.py
python3 6path_summary.py
python3 7path_summary2.py
python3 8category_summary.py
python3 9category_summary2.py
python3 10source_and_destination_category.py

echo "Generating RESULTS ..."

cp article-ids.csv ../
cp category-ids.csv ../
cp article-categories.csv ../
cp edges.csv ../
cp graph-components.csv ../
cp finished-paths-no-back.csv ../
cp finished-paths-back.csv ../
cp percentage-paths-no-back.csv ../
cp percentage-paths-back.csv ../
cp category-paths.csv ../
cp category-subtree-paths.csv ../
cp category-pairs.csv ../

echo "Finished ..."

#!/bin/python3
import io
import json

from fut_mem import counting, parsing

root_cat = parsing.fetch_cat_tree()

root_cat_id = root_cat["id"]

cat_ids = parsing.gather_cat_ids(root_cat)
print(f"Got {len(cat_ids)} cat ids")

all_prods = parsing.fetch_prods(root_cat_id)

print(f"Got {len(all_prods)} prods")

counts = {}
best_seller_lists = {}
swedish_percentages = {}

for id in cat_ids:
    print(f"Counting stuff for cat #{id}")
    cat_prods = parsing.get_cat_prods(all_prods, id)

    counts[id] = len(cat_prods)
    best_seller_lists[id] = counting.best_sellers(cat_prods)
    swedish_percentages[id] = counting.swedish_percent(cat_prods)

with io.open("counts.json", mode="w") as counts_json:
    counts_json.write(json.dumps(counts))

with io.open("best_seller_lists.json", mode="w") as best_seller_lists_json:
    best_seller_lists_json.write(json.dumps(best_seller_lists))

with io.open("swedish_percentages.json", mode="w") as swedish_percentages_json:
    swedish_percentages_json.write(json.dumps(swedish_percentages))

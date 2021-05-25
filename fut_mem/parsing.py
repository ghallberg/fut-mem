from functools import reduce
from operator import add

import requests


def fetch_cat_tree():
    return requests.get("https://mat.se/api/product/getCategoryTree").json()


def fetch_prods(cat_id):
    return requests.get(
        f"https://mat.se/api/product/listByCategory?categoryId={cat_id}"
    ).json()


def get_cat_prods(prods, cat_id):
    return list(
        filter(
            lambda prod: cat_id in [cat_info["id"] for cat_info in prod["categories"]],
            prods,
        )
    )


def gather_cat_ids(cat):
    sub_cats = cat["subCategories"]

    sub_cat_ids = reduce(add, map(gather_cat_ids, sub_cats), [])
    return [cat["id"]] + list(sub_cat_ids)

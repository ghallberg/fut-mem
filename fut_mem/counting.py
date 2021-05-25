import requests


def best_sellers(prods):
    pred = lambda prod: prod["soldCount"]
    prods.sort(key=pred, reverse=True)
    return [prod["id"] for prod in prods[0:5]]


def swedish_percent(prods):
    if len(prods) == 0:
        return -1

    pred = lambda prod: prod["countryOfOrigin"] == "SE"
    swedish_prods = list(filter(pred, prods))
    # Choosing not to round this number.
    return (len(swedish_prods) / len(prods)) * 100

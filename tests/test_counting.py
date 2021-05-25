import io
import json

from fut_mem import counting

bageri_fixture = json.loads(io.open("tests/fixtures/bageri.json").read())


test_prods = [
    {"id": 1, "name": "Papaya", "soldCount": 10, "countryOfOrigin": "US"},
    {"id": 2, "name": "Apple", "soldCount": 54, "countryOfOrigin": "SE"},
    {"id": 3, "name": "Banana", "soldCount": 100000, "countryOfOrigin": "ES"},
    {"id": 4, "name": "Pear", "soldCount": 1, "countryOfOrigin": "SE"},
    {"id": 5, "name": "Orange", "soldCount": 2, "countryOfOrigin": "ES"},
    {"id": 6, "name": "Grapefruit", "soldCount": 15, "countryOfOrigin": "DE"},
    {"id": 7, "name": "Mango", "soldCount": 2000, "countryOfOrigin": "NO"},
    {"id": 8, "name": "Durian", "soldCount": 5, "countryOfOrigin": "NO"},
    {"id": 9, "name": "Sharon", "soldCount": 6, "countryOfOrigin": "NO"},
    {"id": 10, "name": "Lime", "soldCount": 8, "countryOfOrigin": "NO"},
]


def test_best_sellers():
    best_sellers = counting.best_sellers(test_prods)
    assert best_sellers == [3, 7, 2, 6, 1]
    best_sellers = counting.best_sellers(bageri_fixture)
    assert best_sellers == [16959, 16916, 17180, 16944, 24865]


def test_swedish_percent():
    assert counting.swedish_percent(test_prods) == 20
    assert counting.swedish_percent(bageri_fixture) == 57.42574257425742

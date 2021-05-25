from fut_mem import parsing

sub_sub_cat1 = {"id": 3, "subCategories": []}

sub_cat1 = {"id": 1, "subCategories": [sub_sub_cat1]}
sub_cat2 = {"id": 2, "subCategories": []}

test_tree = {"id": 0, "subCategories": [sub_cat1, sub_cat2]}


def test_gather_cat_ids():
    cat_ids = parsing.gather_cat_ids(test_tree)
    id_set = set(cat_ids)
    assert len(cat_ids) == len(id_set)
    assert id_set == {0, 1, 2, 3}


prod1 = {"categories": [{"id": 1, "name": "Frukt"}, {"id": 2, "name": "Godis"}]}
prod2 = {"categories": [{"id": 1, "name": "Frukt"}]}
prod3 = {"categories": [{"id": 0, "name": "Bröd"}]}
prod4 = {"categories": [{"id": 2, "name": "Godis"}]}

prods = [prod1, prod2, prod3, prod4]


def test_get_cat_prods():
    assert parsing.get_cat_prods(prods, 1) == [prod1, prod2]

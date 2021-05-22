# Num prods/cat
  `parent_cat['count'] - sum([cat['count'] for cat in parent_cat['subCategories'])`
# Best sellers
  `order_by prod['soldCount'][0:5(?)]`
# % Swedish
  `prod['countryOfOrigin']`

# Plan
Hämta träd
Rekursera genom trädet och räkna ut ovan data
Medan vi rekurserar bygg upp utträd(dict) med beräknad data
Skriv ut varje utträd som json// dela upp det gemensamma utträdet till tre och skriv ut som json


# Frågor
Träd eller platt lista i output?


#TODO:
  get_cat_prods seems to be broken

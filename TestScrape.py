from scrape import *
from bs4 import BeautifulSoup

name_listSubcategory = []
names = get_categories()

for name in names:

  subcategoryList = get_subcategories(name[1])
  name_listSubcategory.append((name[0], subcategoryList))

with open("dictionary.py", "w") as f:
  f.write("dictionary_list = {}".format(name_listSubcategory))
  f.close()
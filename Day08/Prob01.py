
import re

url = """
https://www.google.com/search?h/petsexpert/siamese-cat-price-in-india/blog/macaws-prices-purchase-cost-supplies-food-and-more/mynextpet.in/macaw-parrot-price-in-india/?result.aspx
"""

while(re.search("/", url)):
    res = re.search("/", url)
    print(url[:res.start()])
    url = url[res.end():]

print(url)

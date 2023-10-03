'''
Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in any order.
'''

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    fav_product = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return_table = fav_product[['product_id']]
    return return_table

# Problem: 
# (10%) Write a Python function named create_data_map
#  that accepts a List of string keys and 
# a List of values. 
# The function must return a Dictionary where the elements of the first list are mapped to the corresponding elements of the second list. Include Type Hints for all arguments (using List, Dict, and Union from the typing module, as appropriate) and the return value. 
# Assume the input lists have the same length.
from typing import List, Dict, Union

def create_data_map(keys: List[str], values: List[Union[str,int,float]]) -> Dict[str, Union[str,int,float]]:
    # arguments:
    # keys:  List[str] -> a list of string type
    # values: a list of values corresponding to each key
    return dict(zip(keys,values))

str_keys = ['id','name', 'age', 'height']
vals = [1,'Tanzim', 33, 5.80]

result = create_data_map(str_keys, vals)

print(result) # Outputs {'id': 1, 'name': 'Tanzim', 'age': 33, 'height': 5.8}

#GITHUB REPO: https://github.com/rahmantanzim/python-101
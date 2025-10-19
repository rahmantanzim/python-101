# 02. Write a Python function named create_data_map
#  that accepts a List of string keys and 
# a List of values. 
# The function must return a Dictionary where the elements of the first list are mapped to the corresponding elements of the second list. Include Type Hints for all arguments (using List, Dict, and Union from the typing module, as appropriate) and the return value. 
# Assume the input lists have the same length.


# def create_data_map(str_keys,vals):
#     dict 
#     for key in str_keys:

#     return 0    

# str_keys = ['id','name', 'age', 'height']
# vals = [1,'Tanzim', 33, 5.80]


from typing import List, Dict, Union
from typing import Any

def create_data_map(keys: List[str], values: List[Union[str, int, float]]) -> Dict[str, Union[str, int, float]]:
    """
    Creates a dictionary mapping each key in 'keys' to the corresponding value in 'values'.

    Args:
        keys (List[str]): A list of string keys.
        values (List[Union[str, int, float]]): A list of values corresponding to each key.

    Returns:
        Dict[str, Union[str, int, float]]: A dictionary mapping keys to values.
    """
    return dict(zip(keys, values))


# Example test
keys_list = ["name", "age", "city"]
values_list = ["Tanzim", 28, "St. John's"]
result = create_data_map(keys_list, values_list)
print(result)



def process_metadata(data_id: str, **kwargs: Any) -> None:
    """
    Prints the data_id and any additional metadata key-value pairs.
    
    Args:
        data_id (str): The required data identifier.
        **kwargs: Optional keyword arguments for metadata settings.
    """
    print(f"Data ID: {data_id}")
    
    # iterate through all key-value pairs in kwargs
    for key, value in kwargs.items():
        print(f"{key}: {value}")
#call the function
process_metadata("Data_Id_01", developer = "Tanzim", version = 1.0, verified = True,location="St. John's")




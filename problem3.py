# 03. Write a Python function named process_metadata that accepts a required positional
# argument data_id and then accepts an arbitrary number of optional keyword arguments to
# store configuration settings. The function should print the data_id and then iterate over and
# print all the received metadata key-value pairs.

from typing import Any

def process_metadata(data_id: str, **kwargs: Any) -> None: 
    print(f"Data ID: {data_id}")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

#call the function

print(process_metadata("Data_Id_01", developer = "Tanzim", version = 1.0, verified = True,location="St. John's"))
import time

#helper function
def create_chunk(chunk_size):
    return list(range(chunk_size))

def make_empty():
    return [] 
    
def with_concatenation(total_chunks = 1000, chunk_size = 100):
    chunk = list(range(chunk_size))
    result = []
    for _ in range(total_chunks):
        result+= chunk
    return result

def with_extension():
    pass

def with_list_comprehension():
    pass
def get_time():
    pass
def benchmark():
    pass
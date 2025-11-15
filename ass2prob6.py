import time

#helper function
def create_chunk(chunk_size):
    result = []
    return list(range(chunk_size))

def create_empty():
    return [] 
    
def with_concatenation(total_chunks = 1000, chunk_size = 100):
    chunk = list(range(chunk_size))
    result = []
    for _ in range(total_chunks):
        result+= chunk
    return result

def with_extension(total_chunks=1000, chunk_size=100):
    chunk = create_chunk(chunk_size)
    result = create_empty() 
    for _ in range(total_chunks):
        result.extend(chunk)
    return result

def with_list_comprehension(total_chunks=1000, chunk_size=100):
    return [
        i * chunk_size + j
        for i in range(total_chunks)
        for j in range(chunk_size)
    ]
def get_time():
    pass
def benchmark():
    pass
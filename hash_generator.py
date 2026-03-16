def generate_hash(input_string):
    hash_value = 0
    
    for char in input_string:
        hash_value+= ord(char)
    return hash_value
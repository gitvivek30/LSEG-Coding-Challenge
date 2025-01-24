def get_value_from_nested_dict(object, key):
    keys = []
    current_key = ''
    
    for char in key:
        if char == '/':
            if current_key:
                keys = keys + [current_key]
                current_key = ''
        else:
            current_key += char
    if current_key:
        keys = keys + [current_key]

    for k in keys:
        found = False
        for key_in_dict in object:
            if key_in_dict == k:
                object = object[key_in_dict]
                found = True
                break
        if not found:
            return "value = null"
    return f"value = {object}"

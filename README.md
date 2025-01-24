# Repository Summary

This repository contains a Python script (`main.py`) that defines the method `get_value_from_nested_dict` to retrieve values from nested dictionaries using a slash-separated key format.

## Description

The `get_value_from_nested_dict(object, key)` function allows you to fetch a value from a nested dictionary. The function takes two parameters:
1. **object**: A nested dictionary where the search will take place.
2. **key**: A string that represents the path to the value, with keys separated by slashes (e.g., `"a/b/c"`).

The function will traverse the dictionary using the given path and return the corresponding value. If the path is not valid, it will return `null`.

## Method Signature & Test Cases

```python
get_value_from_nested_dict(object, key)
Parameters:
object: A nested dictionary.
key: A string representing the path to the value (e.g., "a/b/c").
Returns:
The value located at the provided key path, or null if the key path does not exist.

# Sample Test Case 1 :
Parameters :
object = {"a": {"b": {"c": "d"}}}
key = "a/b/c"
Output:
value = d

# Sample Test Case 2 :
Parameters :
object = {"database": {"host": "localhost", "port": 5432}}
key = "database/host"
Output:
value = localhost

# Sample Test Case 3 :
Parameters :
object = {"database": {"host": "localhost", "port": 5432}}
key = "database/port"
Output:
value = 5432

# Sample Test Case 4 :
Parameters :
object = {"x": {"y": {"z": "a", "l": "m"}}}
key = "x/y/p"
Output:
value = null

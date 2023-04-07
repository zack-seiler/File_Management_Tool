"""
This script allows users to search a directory for a specific term within a
file name and display the search results along with the file path.

It creates a search cache if one does not exist in the specified directory,
to speed up the search process in the future.
"""

import os.path
import time
from os.path import exists
import ast

time_start = time.time()
path = input("Initial Path: ")
search_term = input("Search Term: ")

# converts all files to nested list as dictionary keys and path as values

if not exists(os.path.join(path, "Search Cache.txt")):
    print("No cache found. Creating search cache...")
    files_as_dict = {}
    for directory_path, directory_names, filenames in os.walk(path):
        files_as_dict[str(filenames)] = directory_path

    with open(path + "/Search Cache.txt", 'w', encoding="utf-8") as f:
        f.write(str(files_as_dict))
    f.close()
    print("Search cache created at ", os.path.join(path, "Search Cache.txt"))

with open(path + "\\Search Cache.txt", 'r', encoding="utf-8") as f:
    file_as_string = f.readline()
    dict_to_search = ast.literal_eval(file_as_string)
    f.close()

dict_search_results = {}
dummy_list = []

for key in dict_to_search:
    if search_term.casefold() in key.casefold():
        dummy_list = key
        dummy_list = ast.literal_eval(dummy_list)
        for item in dummy_list:
            # print("Searching: ", item)
            if search_term.casefold() in item.casefold():
                dict_search_results[item] = dict_to_search.get(key)

counter = 0
for key, value in dict_search_results.items():
    counter += 1
    print("Result found: ", key)
    print("At location: ", os.path.realpath(os.path.normpath(value)))
    print()
time_end = time.time()

print(time_end - time_start)
print(counter, " results found")

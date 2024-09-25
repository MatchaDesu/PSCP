"Flatten"
import json
def flatten(x) :
    "flatten"
    for i in x :
        if isinstance(i, list) :
            flatten(i)
        else :
            num_list.append(i)
    return num_list

num_list = []
flatten(json.loads(input()))
num_list.sort(reverse=True)
print(num_list)

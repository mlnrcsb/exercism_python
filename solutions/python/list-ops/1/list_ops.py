def append(list1, list2):
    combined = []
    for item in list1:
        combined += [item]
    for item in list2:
        combined += [item]
    return combined

def concat(lists):
    return [item for sub in lists for item in sub]


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    return sum(1 for item in list)


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function, list, initial):
    list = reverse(list)
    return foldl(function, list, initial)


def reverse(list):
    result = []
    idx = length(list) - 1
    while idx >= 0:
        result += [list[idx]]
        idx -= 1
    return result

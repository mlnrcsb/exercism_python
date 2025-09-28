def flatten_generator(iterable):
    stack = [iterable]
    while stack:
        current = stack.pop()
        if type(current) == list:
            for child in reversed(current):
                stack.append(child)
        else:
            if current is not None:
                yield current

def flatten(arr):
    return list(flatten_generator(arr))

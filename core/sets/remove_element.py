def remove_element(s, element):
    if element in s:
        s.remove(element)
    return s

s = {1, 2, 3}
print(remove_element(s, 2))

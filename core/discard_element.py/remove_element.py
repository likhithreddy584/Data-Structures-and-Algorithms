def remove_element(s, element):
    if element in s:
        s.remove(element)
    return s

s = {10, 20, 30}
print(remove_element(s, 20))
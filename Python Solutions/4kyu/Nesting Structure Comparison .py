def same_structure_as(original, other):
    if isinstance(original, list) and isinstance(other, list):
        if len(original) != len(other):
            return False
        for element, other_element in zip(original, other):
            if same_structure_as(element, other_element) == False:
                return False
    elif isinstance(original, list) or isinstance(other, list):
        return False
    return True
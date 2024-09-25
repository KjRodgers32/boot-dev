def file_type_getter(file_extension_tuples):
    map = {}
    for tuple in file_extension_tuples:
        for extenesions in tuple[1]:
            map[extenesions] = tuple[0]
    return lambda ext: map.get(ext, "Unknown")
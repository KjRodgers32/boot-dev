def zipmap(keys, values):
    if len(keys) == 0 or len(values) == 0:
        return {}
    map = zipmap(keys[1:], values[1:])
    map[keys[0]] = values[0]
    return map
def get_median_font_size(font_size):
    if len(font_size) == 0:
        return None

    sorted_font_size = sorted(font_size)
    middle = len(sorted_font_size) // 2

    if len(sorted_font_size) % 2 == 0:
        return sorted_font_size[middle - 1]
    return sorted_font_size[middle]


def remove_invalid_lines(document):
    doc_to_list = document.split("\n")
    removed_hiphen_lines = filter(lambda x: not x.startswith('-'), doc_to_list)
    return "\n".join(removed_hiphen_lines)
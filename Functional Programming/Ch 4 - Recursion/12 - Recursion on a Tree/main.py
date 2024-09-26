def list_files(current_filetree, current_path=""):
    list_of_paths = []
    for key in current_filetree:
        current_path = f"/{key}"
        if current_filetree[key]:
           list_files(current_filetree[key], current_path)
        else:
           list_of_paths.append(current_path)
    return list_of_paths

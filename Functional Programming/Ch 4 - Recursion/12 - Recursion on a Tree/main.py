def list_files(current_filetree, current_path=""):
   list_of_paths = []
   for key in current_filetree:
      key_to_append = f"/{key}"
      if isinstance(current_filetree[key], type(None)):
         list_of_paths.append(current_path + key_to_append)
      else:
         list_of_paths.extend(list_files(current_filetree[key], current_path + key_to_append))
   return list_of_paths
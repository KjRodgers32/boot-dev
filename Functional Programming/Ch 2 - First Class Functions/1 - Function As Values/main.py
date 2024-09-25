def file_to_prompt(file, to_string):
    string_file = to_string(file)
    return f"```\n{string_file}\n```"

def format_line(line):
    strippd_line = line.strip()
    capital_line = strippd_line.capitalize()
    comma_removed_line = capital_line.replace(',','')
    return f"{comma_removed_line}...."
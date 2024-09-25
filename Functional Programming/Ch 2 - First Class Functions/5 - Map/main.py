def change_bullet_style(document):
    lines_list = document.split("\n")
    alter_list = map(convert_line, lines_list)
    return "\n".join(alter_list)
# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line

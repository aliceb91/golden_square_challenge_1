def make_snippet(string):
    string_list = string.split()
    if len(string_list) > 5:
        return " ".join(string_list[:5]) + "..."
    return string

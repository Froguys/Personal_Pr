def clean_string(filename):
    if filename[-2]=="-":
        filename=filename[:-2]
    if filename.endswith(")"):
        i=filename.rfind("(")
        filename=filename[:i]
    return filename

print(clean_string("Saucisse-1"))
print(clean_string("Saucisse(1)"))
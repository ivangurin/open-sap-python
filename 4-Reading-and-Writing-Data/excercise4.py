cols = 0
rows = 0
chars = []

with open("key.txt", "r") as file:

    lines = file.readlines()

    cols = int(lines[0].strip()) - 1
    rows = int(lines[1].strip())

with open("secret.txt", "r") as file:

    lines = file.readlines()

    s = ""

    for line_index in range(len(lines)):

        s += lines[line_index].strip()

        if len(s) == cols or line_index == len(lines) - 1:
            chars.append(s)
            s = ""

        if len(chars) == rows:
            break

with open("public.txt", "w") as file:

    file.write("\n".join(chars))
    file.write("\n")
    
file = open("raw_dato.txt", "r")
data = file.readline()
data = data.split("\\n")
for i in range(len(data)):
    data[i] = data[i].replace("\\r", "")
    data[i] = data[i].replace("\\t", "")

# Remove tags
for i in range(len(data)):
    tags = []
    for j in range(len(data[i])):
        if data[i][j] == "<":
            begin = j
        if data[i][j] == ">":
            end = j
            tags.append(data[i][begin:end + 1])
    for tag in tags:
        data[i] = data[i].replace(tag, " ")

# Remove leading whitespace
for i in range(len(data)):
    data[i] = data[i].strip()

# Remove empty lines
unempty_lines = []
for i in range(len(data)):
    if data[i].strip() != "":
        unempty_lines.append(data[i])
data = unempty_lines

# Extract and print the name, dob, scores if available
if len(data) >= 10:
    name = data[7] if len(data) > 7 else ""
    dob = data[8] if len(data) > 8 else ""
    scores = data[9] if len(data) > 9 else ""
    data = [name, dob, scores]

# Load unicode tables
chars = [ ]
codes = [ ]

with open("dato.txt", encoding="utf8") as file:
    unicode_tables = file.read().split("\n")

for code in unicode_tables:
    x = code.split(" ")
    if len(x) >= 2:  # Check if x has at least 2 elements
        chars.append(x[0])
        codes.append(x[1])


# Replace special characters in name and scores
for i in range(len(chars)):
    if len(data) >= 3:
        data[0] = data[0].replace(codes[i], chars[i])  # Name
        data[2] = data[2].replace(codes[i], chars[i])  # Scores
for i in range(len(name)):
    if name[i:i+2] == "&#":
        name = name[:i] + chr(int(name[i+2:i+5])) + name[i+6:]

# Write to text.txt
file = open("raw_dato.txt", encoding="utf8", mode="w")
for i in range(len(data)):
    file.write(data[i] + "\n")

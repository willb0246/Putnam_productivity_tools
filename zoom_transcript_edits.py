import  io
keywords = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

just_txt = []
doc_name = ""
output_name = ""

with open(doc_name, "r") as f:
    data = f.readlines()

for x in data:
    if x[0] in keywords:
        pass
    elif x == '\n':
        pass
    else:
        just_txt.append(x)
print(just_txt)

text_write = open(output_name, 'w+')
text_write.writelines(just_txt)
text_write.close()


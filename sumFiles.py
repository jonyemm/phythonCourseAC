
with open("file1.txt") as liste:
    uno = liste.readlines()

with open("file2.txt") as liste:
    dos = liste.readlines()

with open("file3.txt") as liste:
    tres = liste.readlines()

uno.extend(dos)
uno.extend(tres)

with open(r'unides.txt', 'w') as fp:
    for item in uno:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')

# archivos = ["file1.txt", "file2.txt", "file3.txt"]

# with open ("unides.txt", "w") as outfile:
#     for i in archivos:
#         with open(i) as infile:
#             outfile.write(infile.read())
    
#     outfile.write("/n")




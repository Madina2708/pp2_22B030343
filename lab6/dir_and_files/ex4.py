f=open(r"U:\всё\учеба\2024-2025\pp2\pp2-22B030343-YMadina\lab6\dir_and_files\sometext.txt")
cnt=0
for lines in f:
    cnt+=1
print("files has {} lines".format(cnt))
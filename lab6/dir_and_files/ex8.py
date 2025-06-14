import os
p=(r"U:\всё\учеба\2024-2025\pp2\pp2-22B030343-YMadina\lab6\dir_and_files\thisfieiswillbedeleted.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file doesnt exist")
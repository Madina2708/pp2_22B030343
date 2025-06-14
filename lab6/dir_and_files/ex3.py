import os
p=(r"U:\всё\учеба\2024-2025\pp2\pp2-22B030343-YMadina")

if os.path.exists(p):
    print("file and dir portions of the path")
    print(os.path.basename(p))
    print(os.path.dirname(p))
else:
    print("pass doesnt exist!")
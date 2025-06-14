import os
p=os.listdir(r"U:\всё\учеба\2024-2025\pp2\pp2-22B030343-YMadina")

print('Exists:', os.access(__file__, os.F_OK))
print('Readable:', os.access(__file__, os.R_OK))
print('Writable:', os.access(__file__, os.W_OK))
print('Executable:', os.access(__file__, os.X_OK))
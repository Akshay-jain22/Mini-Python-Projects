import re

file = 'My College Email ID is akshayjain.191it102@nitk.edu.in and My Personal Email id is akshayjain222002@gmail.com'

reg = re.findall(r"[A-Za-z0-9._%+-]+"
                 r"@[A-Za-z0-9.-]+"
                 r"\.[A-Za-z]{2-4}", file)
                
print(reg)
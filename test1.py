import os
os.chdir("../")
root = os.getcwd()
os.system("rm test2 -rf")
os.system(f"cd {root}")
os.system("git clone https://github.com/leecqchn/test2.git ")

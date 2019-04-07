import glob

for file_name in glob.glob('*.py'):
    print("File is " + file_name + " and its type is " + str(type(file_name)))

with open('./DB.py') as f:
    print("File is " + str(f) + " and its type is " + str(type(f)))

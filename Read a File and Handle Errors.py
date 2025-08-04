# read_file_task1.py

try:
    with open("sample.txt","r+") as file:
        print("Reading File contents:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

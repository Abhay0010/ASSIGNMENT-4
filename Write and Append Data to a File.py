# write_append_task2.py

filename = "output.txt"

with open(filename, 'w') as file:
    file.write(input("Enter data to write to the file: ") + '\n')

with open(filename, 'a') as file:
    file.write(input("Enter additional data to append: ") + '\n')

print("\nFinal contents of the file:")
with open(filename, 'r') as file:
    for line in file:
        print(line.strip())

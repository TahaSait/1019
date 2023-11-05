sample_File = open("sample.ini")
read_file = sample_File.read()
number_0_to_9 = 0

for char in read_file:
    if char.isdigit():
        number_0_to_9 += 1
print(f"total number count is {number_0_to_9}")
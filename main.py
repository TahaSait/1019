sample_File = open("sample.ini")
read_file = sample_File.read()
number_Counter = 0
vowel_Counter = 0
for char in read_file:
    if char.isdigit():
        number_Counter += 1
    if char in ["a","e","i","o","u"]:
        vowel_Counter += 1


print(f"total number count is {number_Counter}")
print(f"total number count is {vowel_Counter}")

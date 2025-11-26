import os

def rle_encode(text):
    # This makes the text shorter
    result = ""
    count = 1

    # go through every letter
    for i in range(1, len(text)):
        # if same letter, count +1
        if text[i] == text[i-1]:
            count = count + 1
        else:
            # add letter + count
            result = result + text[i-1] + str(count)
            count = 1

    # add last letter group
    result = result + text[-1] + str(count)
    return result


# find txt files
txt_files = []
for f in os.listdir():
    if f.endswith(".txt"):
        txt_files.append(f)

# show menu
print("Choose file:")
for i in range(len(txt_files)):
    print(str(i+1) + ". " + txt_files[i])

# user choose
num = int(input("Number: "))

# check number
if num >= 1 and num <= len(txt_files):

    file_name = txt_files[num - 1]

    # read file (no with)
    f = open(file_name, "r", encoding="utf-8")
    text = f.read()
    f.close()

    text = text.strip()

    # compress
    new_text = rle_encode(text)

    # make new file name
    new_name = file_name.replace(".txt", "_compressed.txt")

    # write file (no with)
    f = open(new_name, "w", encoding="utf-8")
    f.write(new_text)
    f.close()

    print("Done! new file:", new_name)

else:
    print("Wrong number")

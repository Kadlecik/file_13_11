f = open("test1.txt", "w")
f.write("Hello world file")
f.close()

def print_hi(name):

    print(f'Hi, {name}')

f2 = open("test1.txt", "r")
data = f2.read()
f2.close()

if __name__ == '__main__':
    print_hi('PyCharm')


print(data)


def threshold_filter(source_path, output_path, threshold):
    f = open(source_path, "r")
    data = f.read()
    f.close()

    output_data = ""
    for line in data.split("\n"):
        for word in line.split():
            if len(word) > threshold:
                output_data += f"{word}\n"

    f = open(output_path, "w")
    f.write(output_data)
    f.close()


def threshold_filter2(source_path, output_path, threshold):
    with (open(source_path, "r") as source_file,
          open(output_path, "w") as output_file):
        data = source_file.read()

        output_data = ""
        for line in data.split("\n"):
            for word in line.split():
                if len(word) > threshold:
                    output_data += f"{word}\n"

        output_file.write(output_data)




SOURCE_PATH = "data.txt"
FILE_PATH = "filtered.txt"

threshold_filter(SOURCE_PATH, FILE_PATH, 4)


def copy_file(source_path, output_path):
    with (open(source_path, "r") as source_file,
          open(output_path, "w") as output_file):
        output_file.write(source_file.read())

SOURCE_PATH = "data.txt"
FILE_PATH = "copy.txt"

copy_file(SOURCE_PATH, FILE_PATH)

def reverse_file(source_path, output_path):
    with (open(source_path, "r") as source_file,
          open(output_path, "w") as output_file):
        lines = source_file.readlines()
        lines.reverse()
        lines[0] += "\n"
        lines[-1] = lines[-1][:-1]
        output_file.writelines(lines)



SOURCE_PATH = "data2.txt"
FILE_PATH = "copy.txt"

#threshold_filter(SOURCE_PATH, FILE_PATH, 4)
reverse_file(SOURCE_PATH, FILE_PATH)



def find_word(source_path, character):
    with (open(source_path, "r") as source_file,
          open(output_path, "w") as output_file,):
        text = source_file.read()
        words = text.split()

        slova = text.split()
        pocet_slov = sum(1 for slovo in slova if slovo.startswith(output_path))

        porovnavani = [word for word in words if word] if word.lower(). startswith(pismeno)

        count = len(porovnavani)

        output_file.write(f"počet slov začínajících na {písmeno} : {count}\n")

        output_file.write("slova:\n" + "\n".join(porovnavani))

print(f"výsledky byly zapsány do {output_path}")



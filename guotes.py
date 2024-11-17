with open("guotes.txt", 'r', encoding="utf-8") as file:
    for line in file:
        print(line)

author = input("хто автор вірша?")
with open("guotes.txt", 'a', encoding="utf-8") as file:
    file.write("(" + str(author) + ")\n")

while True:
    author = input("Введіть автора: ")
    if author == "ні":
        break
    quote = input("Його цитата: ")

    with open("guotes.txt", 'a', encoding="utf-8") as file:
        file.write(str(author) + ": " + str(quote) + "\n")
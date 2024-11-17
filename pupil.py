class Pupil:
    def __init__(self, surname, name, mark):
        self.surname = surname
        self.name = name 
        self.mark = mark

pupils = []

with open("pupils.txt", 'r', encoding="utf-8") as file:
    for line in file:
        pupil = line.split()
        p = Pupil(pupil[0], pupil[1], pupil[2])
        pupils.append(p)
for p in pupils:
    if p.mark == "5":
        print(p.surname)

s = 0 
for p in pupils:
    s += int(p.mark)
avg = s / len(pupils)
print(avg)
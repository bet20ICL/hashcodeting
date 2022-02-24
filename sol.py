class person:
    def __init__(self, name):
        self.name = name
        self.skills = {}
    def print(self):
        print(self.name)
        for i in self.skills.items():
            print(i)

class project:
    def __init__(self, name, duration, score, deadline):
        self.name = name
        self.score = score
        self.duration = duration
        self.deadline = deadline
        self.roles = {}
    def print(self):
        print(self.name, "score:" + self.score, "duration:" + self.duration, "deadline:" + self.deadline)
        for i in self.roles.items():
            print(i)

projects = []
persons = []

infile = "examples/a_an_example.in.txt"
f = open(infile, "r", encoding = "utf-8")

tmp = f.readline().rstrip()
tmp = tmp.split()

for i in range(int(tmp[0])):
    pline = (f.readline().rstrip()).split()
    tmpp = person(pline[0])
    for j in range(int(pline[1])):
        sline = (f.readline().rstrip()).split()
        tmpp.skills[sline[0]] = sline[1]
    persons.append(tmpp)

for i in persons:
    i.print()

for i in range(int(tmp[1])):
    aline = (f.readline().rstrip()).split()
    tmpa = project(aline[0], aline[1], aline[2], aline[3])
    for j in range(int(aline[-1])):
        rline = (f.readline().rstrip()).split()
        tmpa.roles[rline[0]] = rline[1]
    projects.append(tmpa)

for i in projects:
    i.print()


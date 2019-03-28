class Team:
    name = 'Normal Team'


team1 = Team()
print team1.name

team1.name = "Mobile R&D"
print team1.name

del team1.name
print team1.name

team1.size = 7
print team1.size

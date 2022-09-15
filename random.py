
import random
people = ['brandon', 'elias', 'greg', 'isaia', 'mavrick', 'yohann', 'noah', 'leon', 'anselm', 'john', 'corentin', 'angela','colin','vivian','noah','leon']
number_people = len(people)
number_of_teams = 5

while number_people > 0 and number_of_teams > 0:
    team = random.sample(people, int(number_people/number_of_teams))
for x in team:
    people.remove(x)
    number_people -= int(number_people/number_of_teams)
    number_of_teams -= 1
print(team)
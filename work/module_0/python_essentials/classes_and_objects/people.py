# You could probably use another import here:
from pprint import pprint
import datetime as dt
import statistics as stat


# Person class goes here:
class Person:
    def __init__(self, name, birthdate, height, weight):
        self.name = name
        self.birthdate = birthdate
        self.height = height
        self.weight = weight

    def __repr__(self):
        return "<{}, {}, {}, {}>".format(self.name, self.birthdate, self.height, self.weight)

    def height_inches(self):
        return self.height / 2.54

    def weight_pounds(self):
        return self.weight * 2.2

    def days_until(self, target_age):
        birth_date = dt.datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        target_age_days = dt.timedelta(days=target_age*365).days
        current_age_days = (dt.datetime.now().date() - birth_date).days
        return target_age_days - current_age_days


def dict_builder(alot, key_val):
    return {key_val(elem)[0]: key_val(elem)[1] for elem in alot}


peeps = [Person('Stan', '2008-08-13', 150, 45),
         Person('Kyle', '2008-02-25', 160, 50),
         Person('Cartman', '2008-05-26', 140, 100),
         Person('Kenny', '2009-07-30', 130, 40)]

# Fill in the appropriate expressions in place of the Nones

avg_height = stat.mean([person.height for person in peeps])
print("avg_height: {}cm".format(avg_height))

avg_weight = stat.mean([person.weight for person in peeps])
print("avg_wieght: {}kg".format(avg_weight))

# name2heights = {person.name: person.height for person in peeps}
name2heights = dict_builder(peeps, lambda person: (person.name, person.height))
print("name2heights:")
pprint(name2heights)

# name2weights = {person.name: person.weight for person in peeps}
name2weights = dict_builder(peeps, lambda person: (person.name, person.height))
print("name2weights:")
pprint(name2weights)

peeps_by_age = sorted(peeps, key=lambda person: person.birthdate)
pprint(peeps_by_age)

for person in peeps:
    print(person.name, "days until turn 18 years old: {} days".format(person.days_until(18)))
import pandas as pd
import numpy as np 
import sys, math, random

# column mappings
cols = {
    'name' : 1,
    'class1': 5,
    'class2': 6,
    'class3': 7,
    'class4': 8,
    'class5': 9,
    'partname': 11,
    'partclass1': 15,
    'partclass2': 16,
    'partclass3': 17,
    'partclass4': 18,
    'partclass5': 19,
    }

def get_schedule(data, pair):
  s1 = []
  s2 = []
  if pair[0] == pair[1]:
    # Filled out schedules as partners
    row = pair[0]
    s1 = data.iloc[row, cols['class1'] : (cols['class5'] + 1)].tolist()
    s1 = [ x for x in s1 if type(x) is not float ]
    s2 = data.iloc[row, cols['partclass1'] : (cols['partclass5'] + 1)].tolist()
    s2 = [ x for x in s2 if type(x) is not float ]
  else:
    # Automatically matched
    row = pair[0]
    s1 = data.iloc[row, cols['class1'] : (cols['class5'] + 1)].tolist()
    s1 = [ x for x in s1 if type(x) is not float ]

    row = pair[1]
    s2 = data.iloc[row, cols['class1'] : (cols['class5'] + 1)].tolist()
    s2 = [ x for x in s2 if type(x) is not float ]

  return s1, s2

def has_partner(data_row):
  partname = data_row[cols['partname']]
  return (not type(partname) is float and len(partname.strip().split(' ')) <= 2)

class Participant:
  def __init__(self, name, schedule):
    self.name = name
    self.schedule = schedule

    self.dead = False

  def kill(self):
    self.dead = True

  def __str__(self):
    return ('%s: %s' % (self.name, self.schedule))

  def __repr__(self):
    return self.__str__()

class Pair:
  def __init__(self, part1, part2):
    self.part1 = part1
    self.part2 = part2

  def set_target(self, target):
    self.target = target

  def __str__(self):
    return ('Partner 1: %s\nPartner 2: %s\n' % (self.part1, self.part2))

  def __repr__(self):
    return self.__str__()

def main():
  data = pd.read_csv("data/signups.csv")

  unpartnered = {}
  partners_raw = {}
  for i, row in data.iterrows():
    if has_partner(row):
      name = row[cols['name']]
      partname = row[cols['partname']]
      partners_raw[(name, partname)] = (i, i)
    else:
      unpartnered[row[cols['name']]] = i

  print('unpartnered', unpartnered)

  unpart_names = set(unpartnered.keys())
  while (len(unpart_names)) > 1:
    pair_raw = random.sample(unpart_names, 2)
    unpart_names = unpart_names - set(pair_raw)

    pair = (pair_raw[0], pair_raw[1])
    partners_raw[pair] = (unpartnered[pair[0]], unpartnered[pair[1]])

  print('partners', partners_raw)
  print('unpartnered still', unpart_names)

  partners = []
  for pair_names, pair_rows in partners_raw.items():
    sched1, sched2  = get_schedule(data, pair_rows)

    part1 = Participant(pair_names[0], sched1)
    part2 = Participant(pair_names[1], sched2)

    pair = Pair(part1, part2)
    partners.append(pair)

  print(partners)

if __name__ == '__main__':
  main()


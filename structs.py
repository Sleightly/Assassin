class Participant:
  def __init__(self, name, schedule):
    self.name = name
    self.schedule = schedule

    self.dead = False

  def kill(self):
    self.dead = True

  def schedule_pretty(self):
    sched = ''
    for s in self.schedule:
      sched += ('\n\t%s' % s)
    return sched

  def alive_pretty(self):
    return 'Dead' if self.dead else 'Alive'

  def __str__(self):
    return ('%s (%s):%s' % 
        (self.name, self.alive_pretty(), self.schedule_pretty()))

  def __repr__(self):
    return self.__str__()

class Pair:
  def __init__(self, part1, part2):
    self.part1 = part1
    self.part2 = part2
    self.target = None

  def set_target(self, target):
    self.target = target

  def is_eliminated(self):
    return self.part1.dead and self.part2.dead

  def target_pretty(self):
    if not self.target:
      return 'No target set.'
    return '%s and %s' % (self.target.part1.name, self.target.part2.name)

  def __str__(self):
    return ('Partner 1: %s\nPartner 2: %s\nTarget: %s' 
        % (self.part1, self.part2, self.target_pretty()))

  def __repr__(self):
    return self.__str__()


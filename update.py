import pickle
import time, shutil, argparse

from structs import *

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-k', '--kill', nargs='+', required=False, type=str,
      help='-k name1[ name2]... (surround exact name in quotes)',
      default=[])
  parser.add_argument('-r', '--revive', nargs='+', required=False, type=str,
      help='-r name1[ name2]... (surround exact name in quotes)',
      default=[])

  args = parser.parse_args()

  partners = []
  with open('data/partners.pkl', 'rb') as f:
    partners = pickle.load(f)

  for pair in partners:
    if pair.part1.name in args.kill:
      print('Killing:', pair.part1.name)
      pair.part1.kill()
    if pair.part2.name in args.kill:
      print('Killing:', pair.part2.name)
      pair.part2.kill()
    
    if pair.part1.name in args.revive:
      print('Reviving:', pair.part1.name)
      pair.part1.revive()
    if pair.part2.name in args.revive:
      print('Reviving:', pair.part2.name)
      pair.part2.revive()

  shutil.copyfile('data/partners.pkl',
                  'data/partners.pkl.%s.bak' % time.strftime("%Y-%m-%d_%H:%M"))

  remove_vals = []
  for i, pair in enumerate(partners):
    if pair.is_eliminated():
      remove_vals.append(pair) 
      print('Eliminated', pair)
  for remove in remove_vals:
    partners.remove(remove)

  for i, pair in enumerate(partners):
    pair.set_target(partners[(i + 1) % len(partners)])

  with open('data/partners.pkl', 'wb') as f:
    pickle.dump(partners, f, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
  main()

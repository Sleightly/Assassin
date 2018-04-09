import pickle
import time, shutil

from structs import *

def main():
  partners = []
  with open('data/partners.pkl', 'rb') as f:
    partners = pickle.load(f)

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

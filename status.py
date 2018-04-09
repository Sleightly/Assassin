import pickle

from structs import *

def main():
  partners = []
  with open('data/partners.pkl', 'rb') as f:
    partners = pickle.load(f)

  for pair in partners:
    print(pair)

if __name__ == '__main__':
  main()

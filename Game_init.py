import pandas as pd
import numpy as np 
import sys
import random

df_ppl = pd.read_csv("TBP Assassination.csv")
df_ppl.columns = ["Timestamp", "Your Name", "Your House", "M/I", "Email", "First", "Second", "Third", "Fourth", "Fifth", "Facebook", "pName", "pHouse", "pM/I", "pEmail", "pFirst", "pSecond", "pThird", "pFourth", "pFifth", "pFacebook"]

dict_names = {}
for counter, name in enumerate(df_ppl["Your Name"]):
	dict_names[name] = counter

#print(dict_names)

names = df_ppl["Your Name"]

all_pairs = []

while len(names) > 1:
	pairs = random.sample(set(names), 2)
	names = set(names) - set(pairs)
	all_pairs.append(pairs)
print(all_pairs)

if len(names) > 0:
	print(names)

class Pair:
	def __init__(self, p1, p2, class1, class2):
		self.p1 = p1
		self.p2 = p2
		self.class1 = class1
		self.class2 = class2


dict_classes = {}
class_ids = ["First", "Second", "Third", "Fourth", "Fifth"]
for pair in all_pairs:
	Classes = []
	for cls_id in class_ids:
		Classes.append(df_ppl.loc[dict_names[pair[0]]][cls_id])
	pClasses = []
	for cls_id in class_ids:
		pClasses.append(df_ppl.loc[dict_names[pair[1]]][cls_id])
	dict_classes[pair[0]] = Classes
	dict_classes[pair[1]] = pClasses

print(dict_classes)

#print(df_ppl)


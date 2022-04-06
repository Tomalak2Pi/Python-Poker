# tight player who plays AA-22,AKs-A2s,KQs-KTs,QJs-QTs,JTs,54s+,AKo-A7o,KQo-KJo

print('Please enter a flop: ')
flop = input()

fc1 = flop[0]
fc2 = flop[1]
fc3 = flop[2]

if fc1 == 'A':
 	fc1 = 14
elif fc1 == 'K':
	fc1 = 13
elif fc1 == "Q":
	fc1 = 12
elif fc1 == "J":
	fc1 = 11
elif fc1 == "T":
	fc1 = 10
else:
	fc1 = int(fc1)

if fc2 == 'A':
 	fc2 = 14
elif fc2 == 'K':
	fc2 = 13
elif fc2 == "Q":
	fc2 = 12
elif fc2 == "J":
	fc2 = 11
elif fc2 == "T":
	fc2 = 10
else:
	fc2 = int(fc2)

if fc3 == 'A':
 	fc3 = 14
elif fc3 == 'K':
	fc3 = 13
elif fc3 == "Q":
	fc3 = 12
elif fc3 == "J":
	fc3 = 11
elif fc3 == "T":
	fc3 = 10
else:
	fc3 = int(fc3)

topfc = max(fc1,fc2,fc3)

overpaircombos = 6*(14-topfc)

print('The villain has',overpaircombos,'overpair combinations.')

e = input()

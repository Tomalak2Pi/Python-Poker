# tight player who plays AA-22,AKs-A2s,KQs-KTs,QJs-QTs,JTs,54s+,AKo-A7o,KQo-KJo
totalcombos = 282

while True:
	print('Please enter a flop or type x to quit.')
	flop = input()

	if flop == 'x':
		break

	fc1 = flop[0]
	fc2 = flop[1]
	fc3 = flop[2]

	if fc1 == 'A' or fc1 == 'a':
	 	fc1 = 14
	elif fc1 == 'K' or fc1 == 'k':
		fc1 = 13
	elif fc1 == "Q" or fc1 == 'q':
		fc1 = 12
	elif fc1 == "J" or fc1 == 'j':
		fc1 = 11
	elif fc1 == "T" or fc1 == 't':
		fc1 = 10
	else:
		fc1 = int(fc1)

	if fc2 == 'A' or fc2 == 'a':
	 	fc2 = 14
	elif fc2 == 'K' or fc2 == 'k':
		fc2 = 13
	elif fc2 == "Q" or fc2 == 'q':
		fc2 = 12
	elif fc2 == "J" or fc2 == 'j':
		fc2 = 11
	elif fc2 == "T" or fc2 == 't':
		fc2 = 10
	else:
		fc2 = int(fc2)

	if fc3 == 'A' or fc3 == 'a':
	 	fc3 = 14
	elif fc3 == 'K' or fc3 == 'k':
		fc3 = 13
	elif fc3 == "Q" or fc3 == 'q':
		fc3 = 12
	elif fc3 == "J" or fc3 == 'j':
		fc3 = 11
	elif fc3 == "T" or fc3 == 't':
		fc3 = 10
	else:
		fc3 = int(fc3)

	topfc = max(fc1,fc2,fc3)

	overpaircombos = 6*(14-topfc)
	overpairchance = int(overpaircombos/totalcombos*100)

	print('The villain has',overpaircombos,'overpair combinations.')
	print('He is a pretty tight player, who plays',totalcombos,'possible combos. He therefore has a',overpairchance,'percent chance of an overpair.')
	print('')
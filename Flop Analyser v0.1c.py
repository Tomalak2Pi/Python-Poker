# tight player who plays AA-22,AKs-A2s,KQs-KTs,QJs-QTs,JTs,54s+,AKo-A7o,KQo-KJo
totalcombos = 282

while True:
	print('')
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
	print('But this is before considering card removal.')

	#aces
	acecombos = 6+12*4+7*12 # pocket Aces plus all AXs combos plus 12 x 7 offsuit AX combos

	if fc1 == 14 or fc2 == 14 or fc3 == 14:
		acecomboseliminated = 3+12+7*3 #3 pocket A combos gone, 12 suited As of that suit gone (Ah6h x 12 etc), 7 offsuit x 3 gone too - (AhKc, AhKd, Ahks etc)
		
		print('')
		print('There is an Ace on the board! He plays',acecombos,'combos of Aces and this Ace eliminates',acecomboseliminated,'of them.')
		
		acecombos = acecombos - acecomboseliminated
		totalcombos = totalcombos - acecomboseliminated
		print('Total combos',totalcombos)
		overpairchance = int(overpaircombos/totalcombos*100)

		print('He therefore has a',overpairchance,'percent chance of an overpair.')

	#king
	kingcombos = 6+4*4+3*12 # pocket Ks plus all AKs, KQs-KTs

	if fc1 == 13 or fc2 == 13 or fc3 == 13:
		kingcomboseliminated = 3+3+4*3 #3 pocket A combos gone, 3 suited Ks of that suit gone, 4 offsuit gone too
		
		print('')
		print('There is a King on the board! He plays',kingcombos,'combos of Ks and this King eliminates',kingcomboseliminated,'of them.')
		
		kingcombos = kingcombos - kingcomboseliminated
		totalcombos = totalcombos - kingcomboseliminated
		print('Total combos',totalcombos)
		overpairchance = int(overpaircombos/totalcombos*100)

		print('He therefore has a',overpairchance,'percent chance of an overpair.')
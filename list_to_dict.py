# Converting a list of shortform/slang terms and their respective meaning to a dictionary format
# Acceptable input format:
# 
# ["A:B"]
# ["A,B:C"] (any number of terms, separated by a comma, on the LHS of : but only one term on the RHS)

def listToDict(lst, dct):
	altDict = {}
	d = dct
	for pair in lst:
		#split pair into key and value
		key = pair.split(":")[0]
		value = pair.split(":")[1]
		value = value.strip()

		#check if multiple keys to single value
		if "," in key:
			keys = key.split(",")
			for k in keys:
				if k not in d:
					d[k.strip()] = value
				else:
					altDict[k.strip()] = value
		else:
			if key not in d:
				d[key.strip()] = value
			else:
				d[key.strip()] = value

	print("\n\n ############################# New Dictionary ############################ \n\n")
	print(dict(sorted(d.items())))

	if len(altDict) != 0:
		print("\n\n ############################# Words with existing keys ############################ \n\n")
		print(altDict)

	return d


def main():
	import ast
	lst = input("Enter the list of terms here: ") #paste list to be converted here
	lst = ast.literal_eval(lst)
	currentDict = {'x':'tak', 
                'bodo':'bodoh',
                'bole' : 'boleh',
                'tk' : 'tak',
                'kaseh' : 'kasih',
                'kalo' : 'kalau',
                'xde' : 'tiada',
                'xder' : 'tiada',
                'xnak' : 'tak nak',
                'tknk' : 'taknak',
                'xpe' : 'tidak apa',
                'nk' : 'nak',
                'p' : 'pergi',
                'je' : 'sahaja',
                'shj' : 'sahaja',
                'dgn' : 'dengan',
                'mcm' : 'macam',
                'utk' : 'untuk',
                'blk' : 'balik',
                'nnt' : 'nanti',
                'nape' : 'kenapa',
                'npe' : 'kenapa',
                'esk' : 'esok',
                'drpd' : 'daripada',
                'sbb' : 'sebab',
                'tp' : 'tetapi',
                'da' : 'dah',
                'takde' : 'tiada',
                'tak ada' : 'tiada',
                'kpd' : 'kepada',
                'pd' : 'pada',
                'xtau' : 'tak tahu',
                'abes' : 'habis',
                'aq' : 'aku',
                'ak' : 'aku',
                'apasal': 'kenapa',
                'apesal' : 'kenapa',
                'apahal' : 'kenapa',
                'apehal' : 'kenapa',
                'awk' : 'awak',
                'awl' : 'awal',
                'brp': 'berapa',
                'bape' : 'berapa',
                'bpe' : 'berapa',
                'betol' : 'betul',
                'bhgn' : 'bahagian',
                'bukak': 'buka',
                'buke' :'buka',
                'bkk' : 'buka',
                'bleh' : 'boleh',
                'bley' : 'boleh',
                'blm': 'belum',
                'blom': 'belum',
                'blum' : 'belum',
                'byr' : 'bayar',
                'byk' : 'banyak',
                'camne' : 'bagaimana',
                'cmne' : 'bagaimana',
                'dtg' : 'datang',
                'g' : 'pergi',
                'mslh' : 'masalah',
                'org' : 'orang',
                'kol' : 'call',
                'tu' : 'itu',
                'ni' : 'ini'}
	currentDict = listToDict(lst, currentDict)
	
main()

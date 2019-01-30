import re

def Validate_Card(card):
	valid_structure = r"[456]\d{3}(-?\d{4}){3}$"
	no_four_repeats = r"((\d)-?(?!(-?\2){3})){16}"
	filters = valid_structure, no_four_repeats
	if all(re.match(f, card) for f in filters):
		return True
	else:
		return False

if __name__ == '__main__':
	total_count = int(input("How many Credit Cards would you like to Validate now? "))
	C_Cards = [ input(f"{count+1}. Enter Card Number: ")	for count in range(total_count) ]
	for C_Card in C_Cards:
		valid=Validate_Card(C_Card)
		if valid:
			print(f"\n{C_Card} is Valid Credit Card")
		else:
			print(f"\nSorry, {C_Card} is an Invalid Credit Card, Please Double Check")

def int_to_roman(string):
	""" 4-digit int to roman numeral translator.

	Implements the translation action:

	int -> THOUSANDS HUNDREDS TENS ONES
			{THOUSANDS.T + HUNDREDS.T + TENS.t + ONES.t}

	"""

	string = string.zfill(4)

	thousands, hundreds, tens, ones = string

	result = thousands_to_roman(thousands) + \
				hundreds_to_roman(hundreds) + \
				tens_to_roman(tens) + \
				ones_to_roman(ones)

	return result

def thousands_to_roman(thousands):

	if thousands in ["0","1","2","3"]:
		return "M"*int(thousands)
	else:
		raise NotImplementedError

def hundreds_to_roman(value):
	return order_to_roman(value, "M", "D", "C")

def tens_to_roman(value):
	return order_to_roman(value, "C", "L", "X")

def ones_to_roman(value):
	return order_to_roman(value, "X", "V", "I")

def order_to_roman(value, TEN= "X", FIVE="V", ONE="I"):
	""" Implements the main translation scheme:

	VAL -> 0--3 {VAL.v * ONE}
	VAL -> 4    {ONE + FIVE}
	VAL -> 5--8 {FIVE + (VAL.v - 5) * ONE}
	VAL -> 9    {ONE + TEN}

	where VAL.v = int(VAL) for VAL a one-digit character.
	"""

	if value in ["0","1","2","3"]:
		return ONE*int(value)
	elif value == "4":
		return ONE + FIVE
	elif value in ["5","6","7","8"]:
		return FIVE + ONE*(int(value)-5)
	elif value == "9":
		return ONE + TEN

if __name__ == "__main__":

	value = "1776"

	roman = int_to_roman(value)

	print(roman)

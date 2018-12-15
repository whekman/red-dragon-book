
N = 4

EOFC = '|'

stream = "    E = M * C ** 2 " + EOFC

print("STREAM :=", stream)
print("EOF :=", EOFC)
print("FORWARDP: ^, BEGINP: V")
print()

M = len(stream)

BUFFER = ""

def add_eof_if_necessary(buff, N):
	EOFC = '#'
	if len(buff) < N:
		buff += EOFC
	return buff

BUFFER = BUFFER + stream[:N] + EOFC
stream = stream[N:]

BUFFER = BUFFER + stream[:N] + EOFC
stream = stream[N:]

BEGINP = 0
FORWARDP = 0

def nextchar():
	global FORWARDP
	global BUFFER
	global stream


	FORWARDP += 1
	FORWARDC = BUFFER[FORWARDP]

	end_1st_half = (N + 1) - 1
	end_2nd_half = 2 * (N + 1) - 1

	halt = False

	if FORWARDC is EOFC:

		if FORWARDP is end_1st_half:
			# buffer 2nd half
			print('reload 2nd half')
			BUFFER = BUFFER[:N+1]
			BUFFER = BUFFER + stream[:N] + EOFC
			stream = stream[N:]

			print('remaining stream:', stream)
			# move forward
			FORWARDP += 1
		elif FORWARDP is end_2nd_half:
			# buffer 1st half
			print('reload 1st half')
			BUFFER = BUFFER[N+1:]
			BUFFER = stream[:N] + EOFC + BUFFER
			stream = stream[N:]
			print('remaining stream:', stream)

			# move forward to beginning of 1st half
			FORWARDP = 0

		else:
			print('EOF')
			# actual end of file.
			halt = True

	# halt?
	return halt

def current_lexeme():
	return BUFFER[BEGINP:FORWARDP]

for i in range(32):
	print("  ", " "*BEGINP + 'V')	
	print("B:", BUFFER)
	print("  ", " "*FORWARDP + '^')	
	halt = nextchar()
	if halt:
		break
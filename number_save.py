count = 5200
with open("new_nos1.txt") as f:

	for line in f:
		count += 1
		l = line.strip()
		a = l
		
		with open("00009.txt", "a+") as f1:
			
			f1.write('BEGIN:VCARD\nVERSION:3.0\nN:;%d;;;\nFN:%d\nTEL;TYPE=CELL:%s\nEND:VCARD\n'%(count,count,a))
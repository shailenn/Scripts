count = 4144
with open("new_nos1.txt") as f:
    for line in f:
        count = count + 1
        l = line.split()
		
        contact = l[1]+l[-1]

        intcontact = int(contact)

        sc1 = contact[0:2]
        sc2 = contact[2:4]
        sc3 = contact[4:-1]

        with open("00009.txt", "a+") as f1:
            f1.write('BEGIN:VCARD\nVERSION:2.1\nN:;%d;;;\nFN:%d\nTEL;CELL:%s %s %s\nTEL;CELL:%d\nEND:VCARD\n'%(count,count,sc1,sc2,sc3,intcontact))
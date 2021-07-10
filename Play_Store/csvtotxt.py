def ct(filename, startdate, endate, foldername):
    outname = filename.split(".csv")[0].strip()
    out = open(foldername + outname + ".txt","w+",encoding="utf8")
    out.write("*App_Name :- " + outname + "*\n")
    out.write("*Date :- " + startdate + " " + enddate + "* \n")
    out.write("\n")
    f = open(filename, "r",encoding='mac_roman', newline='')

    nowdate = startdate
    row = "1,3,4,5"
    while True:
        while row and row.split(",")[2] !=  nowdate:
            row = f.readline()

        out.write("*" + nowdate + "*")
        out.write("\n\n")
        while row and row.split(",")[2] == nowdate:
            out.write(row.split(",")[0] + " \n")
            row = f.readline()
        out.write("\n")
        if not row:
            break
        if row and row.split(",")[2] == enddate:
            break
        elif row:
            nowdate = row.split(",")[2]
    f.close()
    out.close()

if __name__ == '__main__':
    foldername = "txtfiles\\" ##  with 
    f = open("csvtotxt.txt", "r+")
    while True:
        filename = f.readline().strip()
        if not filename:
            break
        enddate = f.readline().strip()
        startdate = f.readline().strip()
        ct(filename, startdate, enddate, foldername)
    
    

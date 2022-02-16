import re
import datetime

sixreq = 0
totreq = 0
sixdate = datetime.datetime(1995, 4, 11)

with open("local_copy.log") as file_in:
    for line in file_in:
        logdate  = ""
        datesearch = re.search('../.../....', line)
        if datesearch is not None:
            logdate = datesearch.group(0)
            formlogdate = datetime.datetime.strptime(logdate,'%d/%b/%Y')
            totreq = totreq + 1
            if formlogdate > sixdate:
                sixreq = sixreq +1
print(totreq)
print(sixreq)


DataList =[["Requests last 6 months",sixreq],["Requests overall",totreq]]

print (" Requests from log file sorted ")

for item in DataList:
    print(":",item[0]," "*(22-len(str(item[0]))),":",item[1]," "*(-len(str(item[1]))))

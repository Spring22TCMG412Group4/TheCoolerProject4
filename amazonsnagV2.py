import re
import datetime
import os.path
from urllib.request import urlretrieve

logexists = os.path.exists('local_copy.log')
URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

if not logexists:
    local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)


sixreq = 0
totreq = 0
sixdate = datetime.datetime(1995, 4, 11)

print("Computing...")
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


DataList =[["Requests last 6 months",sixreq],["Requests overall",totreq]]

print (" Requests from log file sorted ")

for item in DataList:
    print(":",item[0]," "*(22-len(str(item[0]))),":",item[1]," "*(-len(str(item[1]))))

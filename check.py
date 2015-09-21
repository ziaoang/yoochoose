

import time
from collections import defaultdict



def Timestamp2Int(Timestamp):
	head = Timestamp[:19]
	tail = Timestamp[20:23]
	return int(time.mktime(time.strptime(head, "%Y-%m-%dT%H:%M:%S"))) * 1000 + int(tail)



print("click")
session_click = {}
for line in open("data/yoochoose-clicks.dat"):
	#1,2014-04-07T10:51:09.277Z,214536502,0
	SeesionID,Timestamp,ItemID,Category = line.strip().split(',')
	if SeesionID not in session_click:
		session_click[SeesionID] = Timestamp2Int(Timestamp)
	else:
		if Timestamp2Int(Timestamp) > session_click[SeesionID]:
			session_click[SeesionID] = Timestamp2Int(Timestamp)


print("buy")
session_buy = {}
for line in open("data/yoochoose-buys.dat"):
	#420374,2014-04-06T18:44:58.314Z,214537888,12462,1
	SessionID,Timestamp,ItemID,Price,Quantity = line.strip().split(',')
	if SeesionID not in session_buy:
		session_buy[SeesionID] = Timestamp2Int(Timestamp)
	else:
		if Timestamp2Int(Timestamp) > session_buy[SeesionID]:
			session_buy[SeesionID] = Timestamp2Int(Timestamp)


for s in session_buy:
	if session_buy[s] < session_click[s]:
		print(s)





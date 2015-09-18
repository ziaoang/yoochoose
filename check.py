

cnt = 0
session = set()
for line in open("data/yoochoose-clicks.dat"):
	cnt += 1
	#1,2014-04-07T10:51:09.277Z,214536502,0
	SeesionID,Timestamp,ItemID,Category = line.strip().split(',')
	session.add(SeesionID)

print(cnt)
print(len(session))


timenow = "23:50:32"

timenow = timenow.split(":")

timenow = [int(i) for i in timenow]
difftime = "21:30:42"
difftime = difftime.split(":")

difftime = [int(i) for i in difftime]

timediff = [a-b for a , b in zip(timenow,difftime)]

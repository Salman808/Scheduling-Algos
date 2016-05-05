#user/bin/python3

arr = []
wait_time = 0
n = int(raw_input('Enter the No. of Process : '))

for i in xrange(n):
	arr.append([])
	print ' '
	arr[i].append(raw_input('Enter Process Name : ' ))
	arr[i].append(int(raw_input('Enter Arrival Time :')))
	arr[i].append(int(raw_input('Enter Burst Time :')))
	arr[i].append(int(raw_input('Enter Priority :')))
	print ' '

time_slice = int(raw_input('Enter the time slice for Process : '))

arr.sort(key = lambda arr:(arr[1],arr[3]))

total = 0
wait = []
finish = []
dup = []

for i in xrange(n):
	finish.append(0)
	total += arr[i][2]
	dup.append(arr[i][2])
	wait.append(0)


j = 0
l = 0

while (l<total):
	j = j % n
	for k in xrange(time_slice):
		if(dup[j] != 0):
			dup[j] -= 1
			l += 1
			if (dup[j] == 0):
				finish[j] = l + arr[j][1] 
				break
	j += 1

for i in xrange(n):
	wait[i]  = finish[i] - arr[i][1] - arr[i][2]

print 'Process Name \tArrival Time \t Burst Time \t  Waiting Time'
for i in xrange(n):
	print arr[i][0] ,'\t\t' ,arr[i][1] ,'\t\t', arr[i][2], '\t\t',wait[i]
	wait_time += wait[i]

print 'Total Waiting Time : ',wait_time
print 'Average Waiting Time : ',(wait_time/n)

#user/bin/python3

arr = []
wait_time = 0
n = int(raw_input('Enter the No. of Process : '))

for i in xrange(n):
	arr.append([])
	print ' '
	arr[i].append(raw_input('Enter Process Name : ' ))
	arr[i].append(int(raw_input('Enter Arrival Time ')))
	arr[i].append(int(raw_input('Enter Burst Time :')))
	print ' '


arr.sort(key = lambda arr:(arr[1],arr[2]))


total = 0
for i in xrange(n): 
	total += arr[i][2]

wait = []
j = 0

while (j<=total):
	service.append(service[j-1] + arr[j-1][2])
	wait.append(service[j] - arr[j][1])
	wait_time += wait[j]
	j += 1

print 'Process Name \tArrival Time \t Burst Time  \t Waiting Time' 
for i in xrange(n):
	print arr[i][0] ,'\t\t' ,arr[i][1] ,'\t\t', arr[i][2], '\t\t',wait[i]

print 'Total Waiting Time : ',wait_time
print 'Average Waiting Time : ',(wait_time/n)

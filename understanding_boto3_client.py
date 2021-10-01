import time
import boto3

start = time.time()

global kuch_aur

t = boto3.client('ec2')
j=1
v = t.describe_instances()["Reservations"]

for i in v:
    u = i["Instances"]
    for k in u:
#        print('{j}. {k}'.format(j=j, k=k["InstanceId"]))
        j+=1

else:
    print(j)
end = time.time()
print(f"Runtime of the program is {end - start}")
import time
import boto3

start = time.time()

global kuch_aur

t = boto3.resource('ec2')
j=1
for i in t.instances.all():
#    print('{j}. {i}'.format(j=j, i=i.id))
    j+=1

else:
    print(j)

end = time.time()
print(f"Runtime of the program is {end - start}")
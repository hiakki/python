import time
import boto3

start = time.time()

global kuch_aur

#s = boto3.Session(profile_name='default')
t = boto3.Session('ec2')
#kuch_aur = s.client('ec2', region_name='ap-southeast-1')


# kuch_aur_2 = kuch_aur.reservations.all()

# for i in kuch_aur_2.instances.all():
#     if i.state['Name'] == 'stopped':
#         print('hello')


for i in t.instances.all():
    if i.state['Name'] == 'stopped':
        print('no hello')
end = time.time()
print(f"Runtime of the program is {end - start}")
import subprocess

a = subprocess.check_output("echo arpit topa", shell = True)
b = subprocess.check_call("echo arpit topa", shell = True)

c = subprocess.check_output("exit 2", shell = True)

print(c)
print('1. {abcd}'.format(abcd=a))
print('2. {xyz}'.format(xyz=a.decode("utf-8")))
print('Status Code - {sc}'.format(sc=b))

import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('nginx_logs','r') as a:
    raw_logs = a.read()

raw_logs = raw_logs.strip()
logs = raw_logs.split('\n')
# print(logs)

group = {}

for log in logs:
    data = log.split(' ')
    client_ip = data[0]
    api_path = data[6]

    if api_path not in group.keys():
        group[api_path] = {}

    if client_ip not in group[api_path].keys():
        group[api_path][client_ip] = 1
    else:
        group[api_path][client_ip] += 1

pp.pprint(group)
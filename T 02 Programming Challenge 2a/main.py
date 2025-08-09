logs = [
    {'username': 'alice', 'ip': '198.168.1.1', 'status': 'success'},
    {'username': 'alice', 'ip': '198.168.1.2', 'status': 'failure'},
    {'username': 'bob', 'ip': '198.168.1.3', 'status': 'success'},
    {'username': 'alice', 'ip': '198.168.1.4', 'status': 'failure'},
    {'username': 'alice', 'ip': '198.168.1.1', 'status': 'success'},
    {'username': 'bob', 'ip': '198.168.1.6', 'status': 'failure'},
    {'username': 'alice', 'ip': '198.168.1.2', 'status': 'success'},
    {'username': 'charlie', 'ip': '198.168.1.8', 'status': 'failure'},
    {'username': 'alice', 'ip': '198.168.1.3', 'status': 'success'},
    {'username': 'bob', 'ip': '198.168.1.10', 'status': 'failure'}
]

unique = set()

for i in range(len(logs)):
    unique.add(logs[i]['ip'])

unique_ip_list = list(unique)
for i in range(len(unique_ip_list)):
    print(unique_ip_list[i])


for i in range(len(logs)):
    if logs[i]['ip'] == '198.168.1.4':
        print("Found the IP Address")
        break
else:
    print("IP Address Not Found")
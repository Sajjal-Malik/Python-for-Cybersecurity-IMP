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

failed_attemps = {}

for log in logs:
    print(log)
    if log['status'] == 'failure':
        username = log['username']
        if username not in failed_attemps:
            failed_attemps[username] = 0
        failed_attemps[username] += 1

print("Failed login attemps per User:", failed_attemps)
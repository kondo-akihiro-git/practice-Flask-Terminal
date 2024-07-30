import requests
import json

def send_command(command):
    url = 'http://127.0.0.1:5000/command'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({'command': command})

    response = requests.post(url, headers=headers, data=data)
    return response.json()

if __name__ == '__main__':
    while True:
        command = input('Enter command: ')
        if command.lower() == 'exit':
            print('Exiting...')
            break
        response = send_command(command)
        print('Response:', response['response'])

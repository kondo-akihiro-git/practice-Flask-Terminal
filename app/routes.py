from flask import Blueprint, request, jsonify, render_template


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/command', methods=['POST'])
def handle_command():
    data = request.json
    command = data.get('command')

    if command == 'hello':
        return jsonify({'response': 'Hello, World!'})
    elif command == 'bye':
        return jsonify({'response': 'Goodbye!'})
    else:
        return jsonify({'response': 'Unknown command'})

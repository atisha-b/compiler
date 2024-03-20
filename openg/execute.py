from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_code():
    try:
        # Get the code from the request
        code = request.json.get('code')

        # Write the code to a temporary file
        with open('temp.py', 'w') as file:
            file.write(code)

        # Execute the Python script using subprocess
        result = subprocess.run(['python', 'temp.py'], capture_output=True, text=True)

        # Check if an error occurred
        if result.stderr:
            return jsonify({'error': result.stderr}), 400
        else:
            return jsonify({'output': result.stdout})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode

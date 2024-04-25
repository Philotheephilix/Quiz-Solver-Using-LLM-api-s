from Solver import connect,input,seggregate
from flask import Flask,request,jsonify,json

app = Flask(__name__)


@app.route("/sendquestion", methods=['GET', 'POST'])
def solver():
    if request.method == 'POST':
        json_data = request.get_json()

        if json_data:

            received_dict = json.loads(json_data)
            input.sent_prompt(received_dict)
            return jsonify({"message": "Data received successfully"}), 200
        else:
            return jsonify({"error": "No JSON data received"}), 400
    else:
        return jsonify({"message": "Send a POST request with JSON data"}), 405

if __name__ == '__main__':
    app.run(debug=True)

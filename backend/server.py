from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/action', methods=['POST'])
def action():
    data = request.json
    user_action = data.get("action", "").lower()

    if "whiskey" in user_action:
        return jsonify({"response": "Olindo beve del whiskey raschio, sbatte la nerchia sul bancone e chiede un rum."})
    elif "iginio" in user_action or "panterona" in user_action:
        return jsonify({"response": "Iginio ignora la missione e va a cercare una panterona brasiliana da conquistare."})
    else:
        return jsonify({"response": f"Hai provato a fare '{user_action}', ma non succede nulla di rilevante."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

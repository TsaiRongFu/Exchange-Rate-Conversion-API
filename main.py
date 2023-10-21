
from flask import Flask, request, jsonify

app = Flask(__name__)

exchange_rates = {
    "currencies": {
        "TWD": {"TWD": 1, "JPY": 3.669, "USD": 0.03281},
        "JPY": {"TWD": 0.26956, "JPY": 1, "USD": 0.00885},
        "USD": {"TWD": 30.444, "JPY": 111.801, "USD": 1}
    }
}

def convert_currency(source, target, amount):
    try:
        exchange_rate = exchange_rates["currencies"][source][target]
        converted_amount = amount * exchange_rate
        return round(converted_amount, 2)
    except KeyError:
        return None

@app.route('/convert', methods=['GET'])
def currency_converter():
    source = request.args.get('source', '')
    target = request.args.get('target', '')
    amount_str = request.args.get('amount', '').replace(',', '')
    try:
        amount = float(amount_str[1:])
    except ValueError:
        return jsonify({"msg": "Invalid amount"}), 400

    converted_amount = convert_currency(source, target, amount)
    if converted_amount is None:
        return jsonify({"msg": "Invalid currency"}), 400

    formatted_amount = "${:.2f}".format(converted_amount)

    return jsonify({"msg": "success", "amount": formatted_amount})

if __name__ == '__main__':
    app.run(debug=True)
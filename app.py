from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extract scores
    math_score = data.get("math score", 0)
    reading_score = data.get("reading score", 0)
    writing_score = data.get("writing score", 0)

    # Calculate average
    average = (math_score + reading_score + writing_score) / 3

    # Determine pass/fail
    result = "pass" if average >= 40 else "fail"

    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(debug=True)







    



 
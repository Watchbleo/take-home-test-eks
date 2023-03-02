from flask import Flask, jsonify

app = Flask(__name__)

# Define your shifts
shifts = [
    {"id": 1, "start_time": "2023-03-01T08:00:00", "end_time": "2023-03-01T16:00:00"},
    {"id": 2, "start_time": "2023-03-01T16:00:00", "end_time": "2023-03-02T00:00:00"},
    {"id": 3, "start_time": "2023-03-02T08:00:00", "end_time": "2023-03-02T16:00:00"},
]

# Define a route that returns the list of shifts
@app.route('/shifts')
def get_shifts():
    return jsonify(shifts)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

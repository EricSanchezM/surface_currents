from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/currents")
def get_surface_currents():
    data = {
        "timestamp": "2025-07-13T12:00:00Z",
        "currents": [
            {"latitude": 34.05, "longitude": -118.25, "speed_m_s": 0.5, "direction_deg": 45},
            {"latitude": 36.12, "longitude": -115.17, "speed_m_s": 0.7, "direction_deg": 90},
            {"latitude": 40.71, "longitude": -74.01, "speed_m_s": 0.3, "direction_deg": 270}
        ]
    }
    return jsonify(data)
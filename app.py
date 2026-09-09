from flask import Flask, jsonify, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/api/tides/<station_id>/<date>', methods=['GET'])
def get_tides(station_id, date):
    try:
        target_date = datetime.strptime(date, '%Y-%m-%d')
        predictions = [
            {
                "eventTime": (target_date + timedelta(hours=6, minutes=30)).isoformat(),
                "height": 4.2,
                "type": "HighWater"
            },
            {
                "eventTime": (target_date + timedelta(hours=12, minutes=45)).isoformat(),
                "height": 1.1,
                "type": "LowWater"
            }
        ]
        return jsonify({"predictions": predictions}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/stations', methods=['GET'])
def list_stations():
    stations = [
        {"stationId": "noaa_8454000", "name": "Battery Park, New York", "latitude": 40.7033, "longitude": -74.0170},
        {"stationId": "sydney_001", "name": "Sydney, Australia", "latitude": -33.8604, "longitude": 151.2093},
        {"stationId": "tokyo_001", "name": "Tokyo, Japan", "latitude": 35.6762, "longitude": 139.6503}
    ]
    return jsonify(stations), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

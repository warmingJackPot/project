# bmi_api.py

from flask import Flask, request, jsonify
from bmi_calculator import calculate_bmi

app = Flask(__name__)

# Простой "хардкод" API-ключа (в реальности — из переменных окружения)
VALID_API_KEY = "secret-bmi-key-123"

def require_api_key():
    """Проверка API-ключа в заголовке запроса."""
    api_key = request.headers.get("X-API-Key")
    if api_key != VALID_API_KEY:
        return False
    return True

@app.route("/api/calculate", methods=["POST"])
def calculate_bmi_api():
    if not require_api_key():
        return jsonify({"error": "Unauthorized: Invalid or missing API key"}), 401

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "JSON body is required"}), 400

        weight = data.get("weight")
        height = data.get("height")

        if weight is None or height is None:
            return jsonify({"error": "Fields 'weight' and 'height' are required"}), 400

        # Расчёт ИМТ
        bmi = calculate_bmi(weight, height)

        # Определение категории
        if bmi < 18.5:
            category = "недостаток веса"
        elif 18.5 <= bmi < 25:
            category = "нормальный вес"
        elif 25 <= bmi < 30:
            category = "избыточный вес"
        else:
            category = "ожирение"

        return jsonify({
            "bmi": bmi,
            "category": category,
            "weight_kg": weight,
            "height_m": height
        }), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
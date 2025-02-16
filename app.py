from flask import Flask, request, jsonify

app = Flask(__name__)

# Game State
game_state = {
    "year": 2025,
    "ai_adoption": 10,
    "workforce_satisfaction": 80,
    "redundancy_rate": 5,
    "compliance_score": 90,
    "budget": 100
}

# Game Actions Mapping
actions = {
    "fast_ai_integration": {"ai_adoption": 20, "workforce_satisfaction": -15, "redundancy_rate": 10, "budget": -15},
    "gradual_ai_training": {"ai_adoption": 10, "workforce_satisfaction": 5, "redundancy_rate": 2, "budget": -10},
    "reskill_redeploy": {"ai_adoption": 5, "workforce_satisfaction": 10, "redundancy_rate": -5, "budget": -20},
    "ai_ethics_compliance": {"compliance_score": 10, "workforce_satisfaction": 5, "budget": -10}
}

@app.route('/game_status', methods=['GET'])
def get_game_status():
    return jsonify(game_state)

@app.route('/choose_action', methods=['POST'])
def choose_action():
    data = request.json
    action = data.get("action")

    if action in actions:
        for key, value in actions[action].items():
            game_state[key] += value

        game_state["year"] += 1  # Progress game

        return jsonify({"message": "Action applied", "new_state": game_state})

    return jsonify({"error": "Invalid action"}), 400

if __name__ == '__main__':
    app.run(debug=True)

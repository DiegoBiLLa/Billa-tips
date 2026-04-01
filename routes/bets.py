from flask import Blueprint, request, jsonify

# Create a blueprint for the bets route
bets_bp = Blueprint('bets', __name__)

# In-memory storage for bets and results
bets = []
results = {}  # Store results for resolved bets

@bets_bp.route('/place_bet', methods=['POST'])
def place_bet():    
    bet_data = request.json
    bet_type = bet_data.get('bet_type')
    amount = bet_data.get('amount')
    # Simulate betting without real balance
    bet = {
        'id': len(bets) + 1,
        'bet_type': bet_type,
        'amount': amount,
        'status': 'pending',
        'potential_winnings': 0  # Placeholder
    }
    # Calculate odds based on bet type and simulate potential winnings
    if bet_type == 'moneyline':
        bet['odds'] = 1.5  # Example odds
    elif bet_type == 'spread':
        bet['odds'] = 1.6
    elif bet_type == 'over_under':
        bet['odds'] = 1.7
    elif bet_type == 'parlay':
        bet['odds'] = 2.0
    elif bet_type == 'live':
        bet['odds'] = 1.8
    else:
        return jsonify({'error': 'Invalid bet type'}), 400
    bet['potential_winnings'] = amount * bet['odds']
    bets.append(bet)
    return jsonify(bet), 201

@bets_bp.route('/resolve_bet/<int:bet_id>', methods=['POST'])
def resolve_bet(bet_id):
    result_data = request.json
    result = result_data.get('result')
    # Store the result
    results[bet_id] = result
    # Update bet status to resolved
    for bet in bets:
        if bet['id'] == bet_id:
            bet['status'] = 'resolved'
            bet['result'] = result
            return jsonify(bet), 200
    return jsonify({'error': 'Bet not found'}), 404

@bets_bp.route('/bet_history', methods=['GET'])
def bet_history():
    return jsonify(bets), 200

@bets_bp.route('/active_bets', methods=['GET'])
def active_bets():
    active = [bet for bet in bets if bet['status'] == 'pending']
    return jsonify(active), 200

# Functionality to calculate odds and potential winnings can be expanded as needed

# Register the bets blueprint in the main app (Assuming there is an app.py)
# from app import app
# app.register_blueprint(bets_bp)
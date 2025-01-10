from flask import Flask, request, jsonify, render_template
from query_data import process_query
from dotenv import load_dotenv
import os

# Load environment variables at startup
load_dotenv()

# Verify OpenAI API key is set
if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("OPENAI_API_KEY environment variable is not set")

app = Flask(__name__)

# Store chat histories for different sessions
chat_histories = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/query', methods=['POST'])
def query():
    data = request.json
    query_text = data.get('query')
    session_id = data.get('session_id', 'default')
    
    if not query_text:
        return jsonify({'error': 'No query provided'}), 400
    
    # Get chat history for this session
    chat_history = chat_histories.get(session_id, [])
    
    try:
        result, updated_history = process_query(query_text, chat_history)
        chat_histories[session_id] = updated_history
        return jsonify(result)
    except Exception as e:
        print(f"Error processing query: {str(e)}")  # Add logging
        return jsonify({'error': str(e)}), 500

@app.route('/api/chat_history', methods=['GET'])
def get_chat_history():
    session_id = request.args.get('session_id', 'default')
    history = chat_histories.get(session_id, [])
    return jsonify({'history': history})

@app.route('/api/clear_history', methods=['POST'])
def clear_history():
    session_id = request.json.get('session_id', 'default')
    if session_id in chat_histories:
        del chat_histories[session_id]
    return jsonify({'message': 'Chat history cleared'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
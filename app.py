# app.py
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Initialize OpenAI client (Replace with your API key)
client = OpenAI(api_key='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')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    try:
        # Create chat completion with OpenAI's new API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        
        # Extract the AI's response
        ai_response = response.choices[0].message.content
        
        return jsonify({"response": ai_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
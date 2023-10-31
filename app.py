from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = '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'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')

    # Use OpenAI API for chatbot response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"You: {user_input}\nBot:",
        max_tokens=150 
    )

    bot_message = response['choices'][0]['text'].strip()

    return bot_message

if __name__ == "__main__":
    app.run(debug=True)

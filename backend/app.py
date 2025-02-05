# from flask import Flask, request, jsonify
# import openai
# import os
# from dotenv import load_dotenv
# from utils.db import Database, log_interaction

# # Load environment variables
# load_dotenv()

# app = Flask(__name__)
# openai.api_key = os.getenv("OPENAI_API_KEY")

# # Initialize the database connection pool
# Database.initialize()

# @app.route("/ask", methods=["POST"])
# def ask_question():
#     user_input = request.json.get("message")

#     # Call ChatGPT API
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a technical interviewer for a DevOps engineer position. Ask relevant questions and evaluate answers."},
#             {"role": "user", "content": user_input}
#         ]
#     )

#     ai_response = response["choices"][0]["message"]["content"]

#     # Log interaction to database
#     log_interaction(user_input, ai_response)

#     return jsonify({"response": ai_response})

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host='0.0.0.0', port=port)


# # @app.route("/ask", methods=["POST"])
# # def ask_question():
# #     user_input = request.json.get("message")

# #     # Call ChatGPT API
# #     response = openai.ChatCompletion.create(
# #         model="gpt-3.5-turbo",
# #         messages=[
# #             {"role": "system", "content": "You are a technical interviewer for a DevOps engineer position. Ask relevant questions and evaluate answers."},
# #             {"role": "user", "content": user_input}
# #         ]
# #     )

# #     ai_response = response["choices"][0]["message"]["content"]

# #     # Optional: Convert AI response to speech
# #     tts = gTTS(text=ai_response, lang="en")
# #     tts.save("response.mp3")
# #     # os.system("start response.mp3")  # Uncomment to play the audio

# #     return jsonify({"response": ai_response})



from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv
from utils.db import Database, log_interaction

# Load environment variables
load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the database connection pool
Database.initialize()

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the AI Interviewer API!"})

@app.route("/ask", methods=["POST"])
def ask_question():
    user_input = request.json.get("message")

    # Call ChatGPT API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a technical interviewer for a DevOps engineer position. Ask relevant questions and evaluate answers."},
            {"role": "user", "content": user_input}
        ]
    )

    ai_response = response["choices"][0]["message"]["content"]

    # Log interaction to database
    log_interaction(user_input, ai_response)

    return jsonify({"response": ai_response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

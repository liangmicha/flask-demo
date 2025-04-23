from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/sale_info_for_chatbot")
def sale_info_for_chatbot():
    print(request.args)
    return {
        "service": "Hiv Prep",
        "cost": "400 KES",
        "patient_first_name": "Josh",
        "pharmacy_name": "Liz's AMAZING pharmacy"
    }

@app.route('/sale_feedback_data', methods=['POST'])
def receive_customer_data(post_id):
    print("sale feedback data persisted: ${request.data}")
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'
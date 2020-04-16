from flask import Flask, jsonify
import aws_controller

application = app = Flask(__name__)

@app.route('/')
def index():
    return "This is the main page."
    
@app.route('/get-items')
def get_items():
    return jsonify(aws_controller.get_items())

@app.route("/post", methods=['GET', 'POST']) 
def put_items():
    aws_controller.put_items()
    return jsonify({
            'Artist':"Bach",
            'SongTitle':'Goldberg Variations'
            } )

if __name__ == '__main__':
    app.run()
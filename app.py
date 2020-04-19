from flask import Flask, jsonify
import aws_controller,os
from flask import Flask, url_for, render_template, redirect,request
from forms import ContactForm

application = app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'



@app.route('/')
def home():
    item = aws_controller.get_items()
    # return jsonify(aws_controller.get_items())
    return render_template('home.html',item = item)


@app.route("/post", methods=['GET', 'POST'])
def post_message():
    form = ContactForm()
    # pass parameters into put_item
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('body')
        # otherwise add to the DB
        aws_controller.put_items(name,message)
        return redirect(url_for('success'))
        
  
    return render_template('post_message.html',form=form,template='form-template')

@app.route('/success', methods=('GET', 'POST'))
def success():
    item = aws_controller.get_items()
    return render_template('success.html',template='success-template',item = item)

if __name__ == '__main__':
    app.run()

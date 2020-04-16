from flask import Flask, jsonify
import aws_controller,os
from flask import Flask, url_for, render_template, redirect,request
from forms import ContactForm

application = app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'


@app.route('/')
def index():
    return render_template('index.html',
                           template='form-template')

@app.route('/get-items')
def get_items():
    return jsonify(aws_controller.get_items())

@app.route("/post", methods=['GET', 'POST'])
def put_items():
    # aws_controller.put_items()
    return jsonify({
            'Artist':"Bob Dylan",
            'SongTitle':'The Hurricane'
            } )


@app.route('/add', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if request.method == 'POST':
        return redirect(url_for('success'))
    return render_template('contact.html',form=form,template='form-template')

@app.route('/success', methods=('GET', 'POST'))
def success():
    return render_template('success.html',
                           template='success-template')

if __name__ == '__main__':
    app.run()
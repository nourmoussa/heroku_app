# import joblib
# import os
# from flask import Flask, jsonify, url_for, send_from_directory

# from flask import request
# from server import predict

# app = Flask(__name__)
# model = joblib.load('reg_1.pkl')


# @app.route('/', methods=['POST'])
# def predict():

#     # Get the data from the POST request.
#     data = request.get_json(force=True)
#     data = [[data["age"], data["gender"], data["height"], data["weight"], data["smoke"], data["alco"], data["active"]]]

#     # Make prediction using model loaded from disk as per the data.
#     prediction = model.predict(data)
#     # Take the first value of prediction
#     output = prediction[0]

#     return {"result": int(output)}

# # @app.route('/favicon.ico')
# # def favicon():
# #     return send_from_directory(os.path.join(app.root_path, 'static'),
# #                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

# if __name__ == '__main__':
#     app.run()

from flask import Flask, render_template, send_file
import joblib
from flask import request
from interpret import show
from io import StringIO

app = Flask(__name__)
model = joblib.load('reg_1.pkl')


@app.route('/', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    data = [data["age"], data["gender"], data["height"], data["weight"], data["smoke"], data["alco"], data["active"]]
    data = [[float(i) for i in data]]

    # Make prediction using model loaded from disk as per the data.
    # Take the first value of prediction
    prediction = model.predict(data)
    # Take the first value of prediction
    output = prediction[0]

    print(type(model))
    lr_local = model.explain_local(data)
    show(lr_local)
    return {"result": int(output)}

@app.route('/recieve_data')
def get_id():
   the_id = Flask.request.args.get('button_id')
   return "<p>Got it!</p>"

@app.route('/', methods=['GET', 'POST'])
def home():
   return Flask.render_template('filename.html')





# data = request.get_json(force=True)
# data = [data["age"], data["gender"], data["height"], data["weight"], data["smoke"], data["alco"], data["active"]]
# data = [[float(i) for i in data]]
# lr_local = model.explain_local(data)

# def fig_to_base64(lr_local):
#     img = io.BytesIO()
#     lr_local.savefig(img, format='png',
#                 bbox_inches='tight')
#     img.seek(0)

#     return base64.b64encode(img.getvalue())
# encoded = fig_to_base64(lr_local)
# my_html = '<img src="data:image/png;base64, {}">'.format(encoded.decode('utf-8'))


# def explain():
#     data = request.get_json(force=True)
#     data = [[data["age"], data["gender"], data["height"], data["weight"], data["smoke"], data["alco"], data["active"]]]

#     print(type(model))
#     lr_local = model.explain_local(data)
#     show(lr_local)
#     return{"lr_local":lr_local}


if __name__ == '__main__':
    app.run()
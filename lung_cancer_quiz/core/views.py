from flask import render_template, redirect, Blueprint, url_for
from lung_cancer_quiz.core.forms import LungCancerForm
import numpy as np
import pickle

core = Blueprint('core',__name__)

@core.route('/')
def index():
    return render_template('index.html')

@core.route('/info')
def info():
    return render_template('info.html')

@core.route('/quiz', methods=['GET','POST'])
def quiz():

    form = LungCancerForm()

    if form.validate_on_submit():
        print("hello")
        responses = np.zeros(15)
        responses[0] = form.gender.data
        responses[1] = form.age.data/100
        responses[2] = form.smoke.data
        responses[3] = form.fingers.data
        responses[4] = form.anxiety.data
        responses[5] = form.pressure.data
        responses[6] = form.chronic.data
        responses[7] = form.fatigue.data
        responses[8] = form.allergies.data
        responses[9] = form.wheezing.data
        responses[10] = form.alcohol.data
        responses[11] = form.cough.data
        responses[12] = form.breath.data
        responses[13] = form.swallowing.data
        responses[14] = form.chest.data

        pickled_model = pickle.load(open('model.pkl', 'rb'))
        responses.shape = (1,15)
        prediction = pickled_model.predict(responses)
        print(prediction)

        return redirect(url_for('core.result',prediction=prediction))

    return render_template('quiz.html',form=form)

@core.route('/<float:prediction>/result')
def result(prediction):
    return render_template('result.html',prediction=prediction)

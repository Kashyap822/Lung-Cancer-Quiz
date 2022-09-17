from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField, RadioField
from wtforms.validators import DataRequired

class LungCancerForm(FlaskForm):
    gender = RadioField('What is your gender?', choices=[(1,'Male'), (0,'Female'), (0.5,'Other')], validators=[DataRequired()])
    age = IntegerField('What is your age?', validators=[DataRequired()])
    smoke = RadioField('Do you smoke?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    fingers = RadioField('Do you have yellow fingers?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    anxiety = RadioField('Do you experience anxiety often?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    pressure = RadioField('Do you experience peer pressure often?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    chronic = RadioField('Do you have chronic disease?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    fatigue = RadioField('Do you experience fatigue often?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    allergies = RadioField('Do you have allergies?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    wheezing = RadioField('Do you experience wheezing?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    alcohol = RadioField('Do you consume alcohol?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    cough = RadioField('Do you cough a lot?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    breath = RadioField('Do you experience shortness of breath?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    swallowing = RadioField('Do you have trouble swallowing?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    chest = RadioField('Do you experience chest pain?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    submit = SubmitField('Submit')

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField,FloatField
from wtforms.validators import DataRequired, Length, Optional
from flask_login import current_user

class Cancer(FlaskForm):
        mean_radius= FloatField('mean radious', validators=[DataRequired()])
        mean_texture=FloatField('mean texture', validators=[DataRequired()])
        mean_perimete=FloatField('mean perimete', validators=[DataRequired()])
        mean_area=FloatField('mean area', validators=[DataRequired()])
        mean_smoothness=FloatField('mean smoothness', validators=[DataRequired()])
        mean_compactness=FloatField(' mean compactness', validators=[DataRequired()])
        mean_concavity=FloatField('mean concavity', validators=[DataRequired()])
        mean_concave_points=FloatField('mean concave points', validators=[DataRequired()])
        mean_symmetry=FloatField('mean symmetry', validators=[DataRequired()])
        mean_fractal_dimension=FloatField('mean fractal dimension', validators=[DataRequired()])
        radius_error=FloatField('radius error', validators=[DataRequired()])
        texture_error=FloatField('texture error', validators=[DataRequired()])
        perimeter_error=FloatField('perimeter error', validators=[DataRequired()])
        area_error=FloatField(' area error', validators=[DataRequired()])
        smoothness_error=FloatField('smoothness error', validators=[DataRequired()])
        compactness_error=FloatField('compactness error', validators=[DataRequired()])
        concavity_error=FloatField('concavity error', validators=[DataRequired()])
        concave_points_error=FloatField('concave points error', validators=[DataRequired()])
        symmetry_error=FloatField('symmetry error', validators=[DataRequired()])
        fractal_dimension_error=FloatField('fractal dimension error', validators=[DataRequired()])
        worst_radius=FloatField('worst radius', validators=[DataRequired()])
        worst_texture=FloatField('worst texture', validators=[DataRequired()])
        worst_perimeter=FloatField('worst perimeter', validators=[DataRequired()])
        worst_area=FloatField(' worst area', validators=[DataRequired()])
        worst_smoothness=FloatField('worst smoothness', validators=[DataRequired()])
        worst_compactness=FloatField('worst compactness', validators=[DataRequired()])
        worst_concavity=FloatField('worst concavity', validators=[DataRequired()])
        worst_concave_points=FloatField('worst concave points', validators=[DataRequired()])
        worst_symmetry=FloatField('worst symmetry', validators=[DataRequired()])
        worst_fractal_dimension=FloatField('worst fractal dimension', validators=[DataRequired()])
        submit=SubmitField('Submit')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, FloatField, RadioField, SelectField
from wtforms.validators import DataRequired, Email, Length


class UserAddForm(FlaskForm):
    """Form for adding users."""
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=8)])


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=8)])

class CategoryForm(FlaskForm):
    """Form for adding categories."""
    
    categoryname = StringField('Category Name', validators=[DataRequired()])
    
class ShowCategoryForm(FlaskForm):
    """Form for Listing categories."""
    categories = RadioField("List of Categories", coerce=int)
    
class SubCategoryForm(FlaskForm):
    """Form for adding sub_categories."""
    subcategoryname = StringField('SubCategory Name', validators=[DataRequired()])
    categories = SelectField("List of Categories", coerce=int)

class ShowSubCategoryForm(FlaskForm):
    """Form for Listing sub-categories."""
    subcategories = RadioField("List of SubCategories", coerce=int)

class TagForm(FlaskForm):
    """Form for adding Tag."""
    tagname = StringField("Tag Name", validators=[DataRequired()])
    # tags = RadioField("Tags", coerce=int)

class ExpenseForm(FlaskForm):
    """Form for adding Expense."""
    expensename = StringField("Expense Name", validators=[DataRequired()])
    timestamp = DateField("Date", validators=[DataRequired()])
    categories = RadioField("Categorie", coerce=int)
    subcategories = RadioField("SubCategory", coerce=int)
    amount = FloatField("Amount", validators=[DataRequired()])
    
    
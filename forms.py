from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, URL, Email
from flask_ckeditor import CKEditorField


# # WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[InputRequired()])
    subtitle = StringField("Subtitle", validators=[InputRequired()])
    img_url = StringField("Blog Image URL", validators=[InputRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[InputRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = EmailField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    name = StringField("Name", validators=[InputRequired()])
    submit = SubmitField('"Friend"')


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Let Me In!")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[InputRequired()])
    submit = SubmitField("Eat This!")


class ContactForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[InputRequired()],
        render_kw={"placeholder": "How should I refer to you? (required)"}
    )
    email = EmailField(
        "Email",
        validators=[InputRequired(), Email()],
        render_kw={"placeholder": "How can I get back to you? (required)"}
    )
    phone = StringField(
        "Phone",
        render_kw={"placeholder": "Want me to give you a call? (optional)"}
    )
    message = TextField(
        "Message",
        validators=[InputRequired()],
        render_kw={"placeholder": "Tell me what's on your mind! (required)"})
    submit = SubmitField("Send Raven")

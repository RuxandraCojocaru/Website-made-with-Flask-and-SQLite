from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, Email
import smtplib
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cat-database1.db'
db = SQLAlchemy(app)


class AddForm(FlaskForm):
    name = StringField('Nume pisică', validators=[DataRequired()])
    age_status = SelectField("Maturitate", choices=['Pui (sub 1 an)', 'Adult (1-10 ani)', 'Bătrână (10+)'])
    color = SelectField("Culoare",
                        choices=['alb', 'negru', 'portocaliu', 'maro', 'gri', 'alb cu negru', 'portocaliu cu alb',
                                 'multicolor'])
    sex = SelectField("Sex", choices=['Femelă', 'Mascul'])
    pedigree = StringField("Rasa", validators=[DataRequired()])
    location = StringField("Locatie (oras, judet)", validators=[DataRequired()])
    img_url = StringField("Link către o poză cu pisica", validators=[DataRequired(), URL(require_tld=True)])
    description = StringField("Descriere", validators=[DataRequired()])
    telephone = StringField("Telefon", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField('Adăugare pisică')


class AdoptionForm(FlaskForm):
    name = StringField('Numele tău', validators=[DataRequired()])
    location = StringField("Localitate (oras, judet)", validators=[DataRequired()])
    telephone = StringField("Telefon", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    description = StringField(
        "Vă rugăm să oferiți câteva detalii despre dvs. și mediul în care doriți să aveți grijă de pisica adoptată. De exemplu: Locuiți la curte sau la apartament? Ați mai avut sau aveți câini, pisici sau alte animale de companie?",
        validators=[DataRequired()])
    submit = SubmitField('Trimitere cerere')


class Filtru(FlaskForm):
    location = StringField("Locatie")
    age_status = SelectField("Maturitate", choices=['', 'Pui (sub 1 an)','Adult (1-10 ani)','Bătrână (10+)'])
    color = SelectField("Culoare", choices=['', 'alb', 'negru', 'portocaliu', 'maro', 'gri', 'alb cu negru', 'portocaliu cu alb', 'multicolor'])
    submit = SubmitField('Aplica filtre')


class Pisica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    age_status = db.Column(db.String(10), nullable=False)
    color = db.Column(db.String(15), nullable=False)
    sex = db.Column(db.String(6), nullable=False)
    pedigree = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(300), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    telephone = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    post_date = db.Column(db.String(250), nullable=False)


def __repr__(self):
    return '<Pisica %r>' % self.id  # genereaza automat id-ul urmator


# db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        pisica = Pisica(
            name=form.name.data,
            age_status=form.age_status.data,
            color=form.color.data,
            sex=form.sex.data,
            pedigree=form.pedigree.data,
            location=form.location.data,
            img_url=form.img_url.data,
            description=form.description.data,
            telephone=form.telephone.data,
            email=form.email.data,
            post_date=str(datetime.datetime.now()).split(" ")[0],
        )
        db.session.add(pisica)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html', form=form)


@app.route('/search', methods=["GET", "POST"])
def search():
    cat_filter = Filtru()
    print(cat_filter.errors)
    print(cat_filter)

    if cat_filter.is_submitted():
        color = cat_filter.color.data
        age = cat_filter.age_status.data
        loc = cat_filter.location.data
        selected_cats = Pisica.query.order_by(Pisica.id.desc()).all()

        if color!="":
            if age!="":
                if loc:
                    selected_cats = Pisica.query.filter(Pisica.color.like(color), Pisica.age_status.like(age), Pisica.location.like(loc)).order_by(Pisica.id.desc())
                else:
                    selected_cats = Pisica.query.filter(Pisica.color.like(color), Pisica.age_status.like(age)).order_by(Pisica.id.desc())
            else:
                if loc:
                    selected_cats = Pisica.query.filter(Pisica.color.like(color), Pisica.location.like(loc)).order_by(Pisica.id.desc())
                else:
                    selected_cats = Pisica.query.filter(Pisica.color.like(color)).order_by(Pisica.id.desc())
        else:
            if age!="":
                if loc:
                    selected_cats = Pisica.query.filter(Pisica.age_status.like(age), Pisica.location.like(loc)).order_by(Pisica.id.desc())
                else:
                    selected_cats = Pisica.query.filter(Pisica.age_status.like(age)).order_by(Pisica.id.desc())
            else:
                if loc:
                    selected_cats = Pisica.query.filter(Pisica.location.like(loc)).order_by(Pisica.id.desc())

        return render_template('search.html', cats=selected_cats, form=cat_filter)


    all_cats = Pisica.query.order_by(Pisica.id.desc()).all()
    return render_template('search.html', cats=all_cats, form=cat_filter)


@app.route('/presentation/<int:cat_id>', methods=["GET", "POST"])
def presentation(cat_id):
    requested_cat = Pisica.query.get(cat_id)
    adoption_form = AdoptionForm()

    if adoption_form.validate_on_submit():
        user_name = adoption_form.name.data
        cat_name = requested_cat.name
        location = adoption_form.location.data
        telephone = adoption_form.telephone.data
        email = adoption_form.email.data
        description = adoption_form.description.data

        email_text = f"Subject:Catville - Ati primit o cerere de adoptie!\n\nBuna ziua, \nCatville va contacteaza in legatura cu anuntul postat de dumneavoastra pe site. " \
                     f"{user_name} vrea sa va adopte pisica {cat_name}! \n" \
                     f"Iata mai multe informatii despre cererea depusa:\n" \
                     f"Localitate: {location} \n" \
                     f"Telefon: {telephone} \n" \
                     f"Email: {email} \n" \
                     f"Mai multe informatii: {description}\n\n" \
                     f"{user_name} asteapta raspunsul dumneavoastra!\nPentru a stopa procesul de trimitere a cererilor de adoptie ulterior adoptarii propriu-zise, dati reply acestui mail. O zi buna!"


        my_email = "email"
        password = "nottoday:)"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=requested_cat.email,
                                msg=email_text)

        return redirect(url_for('home'))

    return render_template('presentation.html', cat=requested_cat, form=adoption_form)


if __name__ == "__main__":
    app.run(debug=True)

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from scrapping import normalize, normalize_dolar
from datetime import datetime

# This links below it's where I collect the actual price fo $BTC and $USDolar.
url = 'https://coinmarketcap.com/currencies/bitcoin/markets/' # $BTC value
url_ = 'https://valor.globo.com/valor-data/' # Price of Dolar in real
dolar = normalize_dolar(url_)
btc = normalize(url)
today = datetime.today()
conversion_result = btc / dolar


# HERE IS THE MAIN FLASK APPLICATION ###

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Converter(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    inpvalue = db.Column(db.Float, unique=False, nullable=False)
    btcvalue = db.Column(db.Float, unique=False, nullable=False)
    usdvalue = db.Column(db.Float, unique=False, nullable=False)
    date_now = db.Column(db.DateTime, default=today)


@app.route('/')
def index():
    # show all data in the DB
    Converter_values = Converter.query.all()
    return render_template('index.html', Converter_values=Converter_values )
    

@app.route("/add", methods=["POST"])
def add():
    # add the input value typed on the application 
    valueinput = request.form.get("valueinput")
    new_input = Converter(inpvalue=valueinput, btcvalue=btc, usdvalue=dolar)
    db.session.add(new_input)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:Converter_id>")
def delete(Converter_id):
    # remove item
    converter = Converter.query.filter_by(id=Converter_id).first()
    db.session.delete(converter)
    db.session.commit()

    return redirect(url_for("index"))


if __name__ == "__main__":
    db.create_all()

    app.run(debug=True)

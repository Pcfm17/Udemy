#importação
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLAlCHEMY_DATE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)

#Modelagem 
#Produto (id, name, price, description)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)


#defenir uma rota raiz(pagina inicial) e a função que será excutada ao requisitar
@app.route('/')

def hello_world():
    return 'hello_world'

if __name__ == "__main__":
    app.run(debug=True)
from flask impor *

class RefeicaoTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nRefeicao = db.Column(db.String(50), unique=False, nullable=True)
    precoRefeicao = db.Column(db.Integer(), unique=True, nullable=True)
    descRefeicao = db.Column(db.Text(), unique=False, nullable=True)

    def __init__(self, name, style, color, quantity, price, updated):
        self.name = name
        self.style = style
        self.color = color
        self.quantity = quantity
        self.price = price
        self.updated = updated
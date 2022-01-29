from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, request, render_template


app = Flask(__name__)

engine = create_engine("postgresql://postgres:postgres@localhost:5432/test")
db = scoped_session(sessionmaker(bind=engine))

app.secret_key = '12345678' #' this key is used to communicate with database.
#Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


@app.route('/', methods=['POST', 'GET'], )
def index():
    if request.method == 'POST':
        product_id=request.form.get("product_id")
        product_name=request.form.get("product_name")
        sale_price=request.form.get("sale_price")
        db.execute("INSERT INTO products (product_id,product_name, sale_price) VALUES (:product_id,:product_name, :sale_price)",
                {"product_id": product_id, "product_name": product_name, "sale_price":sale_price}) 
        db.commit() 
        return render_template("index.html")
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
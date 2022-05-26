from flask import Flask, render_template
import sql
app = Flask(__name__)

print(sql.books)



@app.route('/')
def education_history():

    books = []

    for i in range(len(sql.books)):
        books.append({
            "name": sql.books[i][0],
            "author": sql.books[i][1],
            "date": sql.books[i][2],
            "price": sql.books[i][3],
            "code": sql.books[i][4],
        })

    return render_template("index.html", books_list=books)

    


if __name__ == "__main__":
    app.run(debug=True)
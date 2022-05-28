from flask import Flask, render_template
import sql
app = Flask(__name__)


# add data to books
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

# book page
@app.route('/<name>')
def show_book(name):
    
    for i in range(len(sql.books)):
        if sql.books[i][0] == name:
            var = i;

            return render_template("pages/book.html" , 
                            name = name , 
                            author = sql.books[var][1] , 
                            date = sql.books[var][2] , 
                            price = sql.books[var][3] , 
                            code = sql.books[var][4]
                            )



# register page  
@app.route('/register')
def register():

    

    return render_template("pages/register.html")



# sign in page
@app.route('/sign-in')
def sign():


    return render_template("pages/sign-in.html")



if __name__ == "__main__":
    app.run(debug=True)
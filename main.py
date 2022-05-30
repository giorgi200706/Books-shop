from flask import Flask, render_template , request
import sql
app = Flask(__name__)

books = []
for i in range(len(sql.books)):
    books.append({
        "name": sql.books[i][0],
        "author": sql.books[i][1],
        "date": sql.books[i][2],
        "price": sql.books[i][3],
        "code": sql.books[i][4],
    })

users = []
for i in range(len(sql.users)):
    users.append({
        "name": sql.users[i][0],
        "surname": sql.users[i][1],
        "username": sql.users[i][2],
        "gmail": sql.users[i][3],
        "password": sql.users[i][4],
    })


# add data to books
@app.route('/')
def mainpagebooks():
    
    # sort books by price and output
    books_sort = books
    sort =  request.args.get("sort")
    if sort == "plh":
        for i in range(len(books_sort)):
            for o in range(len(books_sort)):
                if o<i and float(books_sort[o]["price"]) > float(books_sort[i]["price"]) :
                    y = books_sort[i]
                    books_sort[i] = books_sort[o]
                    books_sort[o] = y;
        
        return render_template("index.html", books_list=books_sort)

    elif sort == "phl":
        for i in range(len(books_sort)):
            for o in range(len(books_sort)):
                if o>i and float(books_sort[o]["price"]) > float(books_sort[i]["price"]) :
                    y = books_sort[i]
                    books_sort[i] = books_sort[o]
                    books_sort[o] = y;
        return render_template("index.html", books_list=books_sort)

    else:
        return render_template("index.html", books_list=books)


# book page
@app.route('/<name>')
def show_book(name):
    
    for i in range(len(books)):
        if books[i]["name"] == name:
            var = i;

            return render_template("pages/book.html" , 
                            name = name , 
                            author = books[var]["name"] , 
                            date = books[var]["date"] , 
                            price = books[var]["price"] , 
                            code = books[var]["code"] )
        
    else:
            return render_template("pages/no.html");


# register page  
@app.route('/register' , methods = ["POST" , "GET"])
def register():

    name =  request.args.get("name")
    surname =  request.args.get("surname")
    username = request.args.get("username")
    gmail =  request.args.get("gmail")
    password =  request.args.get("pass")
    submit = request.args.get("submit")

    hello = " "
    if submit == 'Submit':
        k = False
        for i in range(len(users)):
            if users[i]["username"] == username :
                k = True

        if k == False:
            sql.add_users(name , surname , username , gmail , password)
            users.append({
                "name": name,
                "surname": surname,
                "username": username,
                "gmail": gmail,
                "password": password,
            })
            return render_template("pages/register.html" , yes = "You have registered" , no = "")
        else:
            return render_template("pages/register.html" , yes = "" , no = "You are already registered")
    else:
        return render_template("pages/register.html" , yes = "" , no = "")


# sign in page
@app.route('/sign-in')
def sign():

    username =  request.args.get("username")
    password =  request.args.get("password")
    submit = request.args.get("submit")

    mk = 2
    # 1-shevedit
    # 2-ver shevedit

    # return render_template("pages/sign-in.html" , text = "Incorrect password or username")
    

    if submit == "Submit":
        
        for i in range(len(users)):
            if password == users[i]["password"] and username == users[i]["username"]:
                mk = 1

        if mk == 1:
            return render_template("pages/sign-in.html" , yes = "you entered on the account" , no = "")
        else:
            return render_template("pages/sign-in.html" , no = "Incorrect password or username" , yes = "")


    else:
        
        return render_template("pages/sign-in.html" , yes = "" , no = "")
        

@app.route('/add new book')
def addbook():

    name =  request.args.get("name")
    author =  request.args.get("author")
    date = request.args.get("date")
    price =  request.args.get("price")
    code =  request.args.get("code")
    submit = request.args.get("submit")

    if submit == 'Submit':
        k = False
        for i in range(len(books)):
            if books[i]["name"] == name :
                k = True

        if k == False:
            sql.add_books(name , author , date , price , code)
            books.append({
                "name": name,
                "author": author,
                "date": date,
                "price": price,
                "code": code,
            })
            return render_template("pages/add-book.html" , yes = "The book was added" , no = "")
        else:
            return render_template("pages/add-book.html" , yes = "" , no = "We already have this book")
    else:
        return render_template("pages/add-book.html" , yes = "" , no = "")


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template , request
import sql
app = Flask(__name__)


# add data to books
@app.route('/')
def mainpagebooks():

    books = []
    for i in range(len(sql.books)):
        books.append({
            "name": sql.books[i][0],
            "author": sql.books[i][1],
            "date": sql.books[i][2],
            "price": sql.books[i][3],
            "code": sql.books[i][4],
        })
    
    # sort books by price and output
    books_sort = books
    sort =  request.args.get("sort")
    if sort == "plh":
        for i in range(len(books_sort)):
            for o in range(len(books_sort)):
                if o<i and books_sort[o]["price"] > books_sort[i]["price"] :
                    y = books_sort[i]
                    books_sort[i] = books_sort[o]
                    books_sort[o] = y;
        
        return render_template("index.html", books_list=books_sort)

    elif sort == "phl":
        for i in range(len(books_sort)):
            for o in range(len(books_sort)):
                if o>i and books_sort[o]["price"] > books_sort[i]["price"] :
                    y = books_sort[i]
                    books_sort[i] = books_sort[o]
                    books_sort[o] = y;
        return render_template("index.html", books_list=books_sort)

    else:
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
                            code = sql.books[var][4])




# register page  
@app.route('/register')
def register():

    

    return render_template("pages/register.html")



# sign in page
@app.route('/sign-in')
def sign():

    # create users dictionary andd fill
    users = []
    for i in range(len(sql.users)):
        users.append({
            "name": sql.users[i][0],
            "surname": sql.users[i][1],
            "username": sql.users[i][2],
            "gmail": sql.users[i][3],
            "password": sql.users[i][4],
        })

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
        


if __name__ == "__main__":
    app.run(debug=True)
import sqlite3
database = 'shop.db'
con = sqlite3.connect('shop.db', check_same_thread=False)
cur = con.cursor()

#                                                                                                  GHS653VBA62
# cur.execute('''insert into books values ("The Anubis Gates" , "Tim Powers" , 1983 , 12.99 ,     "3GV72B7CBV") ''')

cur.execute('''create table phones (company text , fullname text , memory text , color text , date text , size text , weight text , simcard text ,  screensize text , screenresolution text , operatingsystem text , chipset text , gpu tetx , internammemory text , ram text ,  additionalmemory text , maincamera text ,  video text , selfiecamera text , selfievideo text , bluthooth text , gps text , nfc text , fmradio text ,  port text ,sizemah text)''')
# cur.execute('''create table usrs (name text , surname text , gmail text , password text)''')

# get data from books
data = cur.execute("select * from books")
items  = cur.fetchall()
books = items;

# get data from work
data = cur.execute("select * from users")
items  = cur.fetchall()
users = items;

# function which add users in database
def add_users(name , surname , username , gmail , password):
    cur.execute("INSERT INTO users (name , surname , username , gmail , password) VALUES (? , ? , ? , ? , ?)" , (name , surname , username , gmail , password))
    con.commit();

# function which add users in database
def add_books(name , author , date , price , code):
    cur.execute("INSERT INTO books (name , author , date , price , code) VALUES (? , ? , ? , ? , ?)" , (name , author , date , float(price) , code))
    con.commit();

con.commit()
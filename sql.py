import sqlite3
database = 'shop.db'
con = sqlite3.connect('shop.db')
cur = con.cursor()

#                                                                                                     GHS653VBA62
# cur.execute('''insert into books values ("Adventure" , "Jack London" , 1911 , 16.99 , "LFVB643V637") ''')
# cur.execute('''insert into books values ("The Little Lady of the Big House" , "Jack London" , 1915 , 18.99 , "B43BV73NF74") ''')
# cur.execute('''insert into books values ("The Game" , "Jack London" , 1905 , 7.99 , "V23NF82NF44") ''')


# get data from books
data = cur.execute("select * from books")
items  = cur.fetchall()
books = items;

# get data from work
data = cur.execute("select * from users")
items  = cur.fetchall()
users = items;


con.commit()
con.close()
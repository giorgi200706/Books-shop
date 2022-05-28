import sqlite3
database = 'shop.db'
con = sqlite3.connect('shop.db')
cur = con.cursor()

#                                                                                                  GHS653VBA62
# cur.execute('''insert into books values ("The Anubis Gates" , "Tim Powers" , 1983 , 12.99 ,       "3GV72B7CBV") ''')



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
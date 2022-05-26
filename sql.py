import sqlite3
database = 'shop.db'
con = sqlite3.connect('shop.db')
cur = con.cursor()

#                                                                                                 GHS653VBA62
# cur.execute('''insert into books values ("To Kill a Mockingbird" , "Harper Lee" , 2006 , 10.99 , "GYFD65B2VED") ''')
# cur.execute('''insert into books values ("The Diary of a Young Girl" , "Anne Frank" , 1942 , 9.99 , "GB437343264") ''')
# cur.execute('''insert into books values ("Animal Farm" , "George Orwell" , 1945 , 12.99 , "34VG5V7F7VB") ''')
# cur.execute('''insert into books values ("The Little Prince" , "Antoine de Saint-Exupéry" , 1943 , 7.99 , "34BYV76G5YB") ''')
# cur.execute('''insert into books values ("The Great Gatsby" , "F. Scott Fitzgerald" , 1925 , 12.99 , "RB6T43FV543") ''')
# cur.execute('''insert into books values ("The Lord of the Rings" , " J.R.R. Tolkien" , 1955 , 15.99 , "F7YGY34GGVG") ''')


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
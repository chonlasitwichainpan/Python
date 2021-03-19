import sqlite3
#conn = sqlite3.connect (r"D:\WorkKKU\1_2\ED251007\Chonlasit_Python\week6.db")
#c = conn.cursor()
#c.execute ('''INSERT INTO users (id,fname,lname,email) VALUES (NULL,"A","A","A")''')
#c.execute ('''INSERT INTO users VALUES (NULL,"B","B","B")''')
#conn.commit ()
#conn.close ()

def insertTouser (fname,lname,email) :
    try :
        conn = sqlite3.connect (r"D:\WorkKKU\1_2\ED251007\Chonlasit_Python\week6.db")
        c = conn.cursor ()

        sql = '''INSERT INTO users (fname,lname,email) VALUES (?,?,?) '''
        data = ('fname','lname','email')
        c.execute(sql,data)
        c.execute ('INSERT INTO users (fname,lname,email) VALUES (?,?,?)',data)
        conn.commit ()
        c.close ()

    except sqlite3.Error as e:
        print ('Failed to insert : ',e)
    finally :

        if conn :
            conn.close ()

insertTouser ('aaa','bbb','ccc')
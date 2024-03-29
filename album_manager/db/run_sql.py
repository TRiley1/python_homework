import psycopg2
import psycopg2.extras as ext

def run_sql(sql, values=None):
    # setup a variable for the connection
    conn = None
    # set up an empty list 
    results = []
    # try to connect to database 
    try: 
        conn = psycopg2.connect("dbname = 'album_manager'")
        # get a cursor
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        # execute the sql 
        cur.execute(sql, values)
        # commint the execution
        conn.commit()
        # get results
        results = cur.fetchall()
        # close the db connection
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return results
    # return the list 
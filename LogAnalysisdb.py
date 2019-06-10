# !/usr/bin/env python


import psycopg2
# month={'01':"january",'02':"February",'03':"March",'04':"April",'05':"May",'06':"June",'07':"July",'08':"August",'09':"Septemper",'10':"October",'11':"November",'12':"December"}

if __name__ == '__main__':
    # connecting to database news
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    # To print the most popular three articles of all time
    c.execute("select title, count(title) as hits from articles left join "
              "log on '/article/' || articles.slug = log.path group by"
              " log.path,articles.title order by hits desc limit 3;")
    print("\nThe most popular three articles of all time are:")
    for i in c.fetchall():
        print("{} -- {} views".format(i[0], i[1]))

    print("\nThe most popular article authors of all time are:")

    # to print most popular article authors of all time
    c.execute("select name,count(path) as views from authors left join "
              "articles on articles.author=authors.id left join log on "
              "log.path= '/article/'||articles.slug group by authors.id "
              "order by views desc ;")
    for i in c.fetchall():
        print("{}-- {} views".format(i[0], i[1]))

    print("\nDays with more than 1% of requests that lead to errors")
    c.execute("select TO_CHAR(a.day, 'Mon DD, YYYY'), round(cast(errorcount as"
              " decimal)/totalcount*100,2) from (select Date(time) as "
              "day,count(*) as errorcount from log where not status like "
              "'200%'group by day ) as a, (select Date(time) as day, count(*)"
              " as totalcount from log group by day ) as b where a.day=b.day "
              "and cast(errorcount as decimal)/totalcount*100 >1")
    for i in c.fetchall():
        # j=i[0]
        print("{}  -{}%\n".format(i[0], i[1]))

    db.close()

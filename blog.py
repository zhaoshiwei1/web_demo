import time
import web

from model import *

urls = (
    '/','index',
    '/add','add',
    )

class index:
    def GET(self):
        s = ""
        sdb = sqldb()
        rec = sdb.cu.execute("""SELECT * FROM WEB_TEST""")
        dbre = sdb.cu.fetchall()
        for i in dbre:
            s = "<p>" + "<span>" + i[1] + "</sapn >" + "<span>" + i[2] + "</sapn >" + "<span>" + i[3] + "</span>"+"<span>" + i[3] + "</span>" +"</p>" + s

        sh = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"><HTML>
        <HEAD><meta http-equiv="X-UA-Compatible" content="IE=8" />
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <TITLE> OK!</TITLE> </HEAD> <BODY><h1>Hello World!</h1>
        """
        sb = """
        <h2>add a note</h2>
        <form method="post" action="/add">
        UserName:<INPUT TYPE="text" NAME="uname"><br />
        <textarea name="content" ROWS="20" COLS="60"></textarea><br />
        <button type="submit">save</button></form></BODY></HTML>
        """
        s = sh + s + sb
        return s

class add:
    def POST(self):
        i = web.input('content')
        n = web.input('uname')
        date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        sdb = sqldb()
        t = (n.uname,date,i.content)
        sdb.cu.execute('insert into WEB_TEST(NAME, CONTENT, DTIME) values(?,?,?)',t)
        sdb.conn.commit()
        return web.seeother('/')
    def GET(self):
        return web.seeother('/')


if __name__=="__main__":
    app = web.application(urls,globals())
    app.run()
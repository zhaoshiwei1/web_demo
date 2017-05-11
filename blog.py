#-*- coding: UTF-8 -*-
# 技术验证完成， 最后一次提交
import time
import web
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from model import *

urls = (
    '/','index',
    '/add','add',
    '/new','new',
    '/delete', 'delete'
    )

class index:
    def GET(self):
        s = ""
        sdb = sqldb()
        rec = sdb.cu.execute("""SELECT * FROM WEB_TEST""")
        dbre = sdb.cu.fetchall()
        col_name_list = [tuple[0] for tuple in rec.description]
        s = s + """<table width="77%" border="0">"""
        s = s + """<tr>"""
        for l in col_name_list:
            s = s + """<th align="left">"""
            # 数据库列名拼接到表格中
            s = s + l
            s = s + """</th>"""
        s = s + """<th align = "left">"""
        s = s +""" </th>"""
        s = s + """</tr>"""
        for i in dbre:
            s = s + """<tr><form action="" method = "post">"""
            for j in range(len(i)):
                s = s + """<td nowrap align="left">"""
                if j ==0:
                    s = s + """<INPUT TYPE="text" NAME="id" value = """+str(i[j])+""" disabled="true">"""
                else:
                    s = s + str(i[j])
                s = s + """</td>"""
            s = s + """<td><button type="submit">编辑</button><button type="submit" formaction="/delete">删除</button></td></form>"""
            s = s + """</tr>"""
        s = s + """</table>"""
        s = s + """
        <form method="get" action="/new"><button type="submit"> 添加 </button></form>
        """
        sh = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"><HTML>
        <HEAD><meta http-equiv="X-UA-Compatible" content="IE=8" />
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <TITLE> 后台接口测试平台</TITLE> </HEAD> <BODY><h1>Welcome!</h1>
        """
        sb = """
        </BODY></HTML>
        """
        s = sh + s + sb
        return s

class add:
    def POST(self):
        i = web.input('content')
        n = web.input('uname')
        date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        sdb = sqldb()
        t = (n.uname,i.content,date)
        sdb.cu.execute('insert into WEB_TEST(NAME, CONTENT, DTIME) values(?,?,?)',t)
        sdb.conn.commit()
        return web.seeother('/')
    def GET(self):
        return web.seeother('/')

class new:
    def GET(self):
        sh = """
            <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"><HTML>
            <HEAD><meta http-equiv="X-UA-Compatible" content="IE=8" />
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <TITLE> 后台接口测试平台</TITLE> </HEAD> <BODY><h1>Welcome!</h1>
            """
        sb = """
            </BODY></HTML>
            """
        s = """
        <h2>新增</h2>
            <form method="post" action="/add">
            UserName:<INPUT TYPE="text" NAME="uname"><br />
            <textarea name="content" ROWS="20" COLS="60"></textarea><br />
            <button type="submit">save</button></form>
        """
        return sh + s + sb

class delete:
    def POST(self):
        i = web.input('id')
        print i.id
        sdb = sqldb()
        sdb.cu.execute('DELETE FROM web_test where ID ='+i.id)
        sdb.conn.commit()
        return web.seeother('/')

if __name__=="__main__":
    app = web.application(urls,globals())
    app.run()
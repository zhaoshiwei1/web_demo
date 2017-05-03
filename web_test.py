import web
from web import form
# http://www.cnblogs.com/xiaowuyi/archive/2012/11/15/2771099.html
# http://blog.csdn.net/freeking101/article/details/53020728
render = web.template.render('templates/')
urls = (
    # '/(.*)', 'index',
    '/', 'home',
)
app = web.application(urls, globals())

login = form.Form(
    form.Textbox('username'),
    form.Password('password'),
    form.Password('password_again'),


    form.Button('Login'),
    form.Checkbox('YES'),
    form.Checkbox('NO'),
    form.Textarea('moe'),
    form.Dropdown('SEX', ['man', 'woman']),
    form.Radio('time',['2012-01-01','20120101']),
    validators = [form.Validator("Passwords didn't match.", lambda i: i.password == i.password_again)]
)

#
#
# class index:
#     def GET(self, name):
#         i=web.input(name=None)
#         return render.index(name)

class home:
    def GET(self):
        f=login()
        return render.formtest(f)
    def POST(self):
        f=login()
        if not f.validates():
            return render.formtest(f)
        else:
            return "HAHA!"

if __name__ == "__main__":
    app.run()
import web
# http://www.cnblogs.com/xiaowuyi/archive/2012/11/15/2771099.html
urls = (
    '/(.*)', 'hello'
)

class hello:
    def GET(self, parameter):
        return "HELLO: World!" + parameter


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
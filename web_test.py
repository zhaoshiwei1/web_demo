import web

urls = (
    '/(.*)', 'hello'
)

class hello:
    def GET(self, parameter):
        return "HELLO: World!" + parameter


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
# coding: utf-8
import os.path
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options

import config
from controllers import post, user, reply
from database import create_db
from helpers import getAvatar

config = config.rec()
define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", post.HomeHandler),
            (r"/page/(\d+)[/]*", post.HomeHandler),

            (r"/archive[/]*", post.ArchiveHandler),
            (r"/archive/page/(\d+)[/]*", post.ArchiveHandler),

            (r"/post/(\d+)[/]*", post.PostHandler),
            (r"/post/add[/]*", post.PostAddHandler),
            (r"/post/edit/(\d+)[/]*", post.PostEditHandler),

            (r"/reply/(\d+)/add[/]*", reply.ReplyAddHandler),
            (r"/reply/(\d+)/edit/(\d+)[/]*", reply.ReplyEditHandler),

            (r"/rss[/]*", post.FeedHandler),
            (r"/feed[/]*", post.FeedHandler),

            (r"/login[/]*", user.LoginHandler),
            (r"/logout[/]*", user.LogoutHandler),

        ]
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            ui_modules={"RecentReplys": post.RecentReplysModule},
            xsrf_cookies = True,
            cookie_secret = config.cookie_secret,
            autoescape = None,
            title = config.title,
            desc = config.description,
            name = config.name,
            admin_username = config.admin_username,
            admin_avatar_url = getAvatar(config.admin_email, 96),
            admin_info = config.admin_info,
            url = config.url,
            login_url = "/",
            paged = config.paged,
            recent_replys = post.getRecentReplys()
        )
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    create_db()
    print("App started. Listenning on %d" % int(os.environ.get('PORT', 8888)))
    tornado.options.parse_command_line()
    tornado.httpserver.HTTPServer(Application(),
            xheaders=True).listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()

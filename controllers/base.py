# coding: utf-8

import tornado.web

import config

config = config.rec()

class BaseHandler(tornado.web.RequestHandler):
    def on_finish(self):
        None

    def get_current_user(self):
        username = self.get_secure_cookie("user")
        if username:
            return tornado.escape.json_decode(username)
        else:
            return None

    def set_current_user(self, username):
        if username:
            self.set_secure_cookie("user",
                    tornado.escape.json_encode(username))
        else:
            self.clear_cookie("user")

    def set_replyer(self, name, email, website):
        if name:
            self.set_secure_cookie("replyer",
                    tornado.escape.json_encode({'name': name, 'email': email,
                        'website': website}))
        else:
            self.clear_cookie("replyer")

    def get_replyer(self):
        name = self.get_secure_cookie("replyer")
        if name:
            return tornado.escape.json_decode(name)
        else:
            return None

    def auth_user(self, username, password):
        return username == config.admin_username and password == config.admin_password

    def is_admin(self):
        return self.get_current_user() == config.admin_username

    def check_admin(self):
        if not self.is_admin():
            raise tornado.web.HTTPError(404)

    def get_current_user(self):
        return self.get_current_user()

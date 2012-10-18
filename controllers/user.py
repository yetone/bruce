# coding: utf-8


import config
from .base import BaseHandler


config = config.rec()

class LoginHandler(BaseHandler):
    def get(self):
        if self.isAdmin():
            self.redirect("/")
        else:
            self.render("login.html")

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        if self.userAuth(username, password):
            self.currentUserSet(username)
            self.redirect("/")
        else:
            self.redirect("/login")

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie('user')
        self.redirect('/login')


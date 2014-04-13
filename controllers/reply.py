# coding: utf-8

import config
from .base import BaseHandler
from helpers import formatText
from extensions import md
from database import db
import tornado.web

from models import Reply, Post


config = config.rec()

class ReplyAddHandler(BaseHandler):
    def post(self, pid):
        name = self.get_argument("reply[name]", default='')
        email = self.get_argument("reply[email]", default='')
        website = self.get_argument("reply[website]", default='')
        origin_content = self.get_argument("reply[content]", default='')
        content = formatText(md(formatText(origin_content)))
        if name == "":
            self.redirect("/post/%d" % int(pid), error=u"请填入名字")
        if email == "":
            self.redirect("/post/%d" % int(pid), error=u"请填入邮箱地址")
        if origin_content == "":
            self.redirect("/post/%d" % int(pid), error=u"请输入评论内容")
        number = db.query(Reply).filter(Reply.pid == pid).count() + 1
        db.add(Reply(pid=int(pid), name=name, email=email, website=website,
            content=content, origin_content=origin_content, number=number))
        db.commit()
        self.set_replyer(name, email, website)
        self.redirect("/post/%d#%d" % (int(pid), int(number)))

class ReplyEditHandler(BaseHandler):
    def get(self, pid, id):
        self.check_admin()
        reply = db.query(Reply).get(id)
        if reply is None:
            raise tornado.web.HTTPError(404)
        post = db.query(Post).get(reply.pid)
        self.render("replyedit.html", reply=reply, post=post)

    def post(self, pid, id):
        self.check_admin()
        name = self.get_argument("reply[name]", default='')
        email = self.get_argument("reply[email]", default='')
        website = self.get_argument("reply[website]", default='')
        origin_content = self.get_argument("reply[content]", default='')
        content = md(formatText(origin_content))
        if name == "":
            self.redirect("/post/%d" % int(pid), error=u"请填入名字")
        if email == "":
            self.redirect("/post/%d" % int(pid), error=u"请填入邮箱地址")
        if origin_content == "":
            self.redirect("/post/%d" % int(pid), error=u"请输入评论内容")
        reply = db.query(Reply).get(id)
        if reply is None:
            raise tornado.web.HTTPError(404)
        reply.name = name
        reply.email = email
        reply.website = website
        reply.origin_content = origin_content
        reply.content = content
        db.commit()
        self.set_replyer(name, email, website)
        self.redirect("/post/%d#%d" % (int(pid), int(reply.number)))

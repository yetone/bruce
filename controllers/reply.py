# coding: utf-8

import config
from .base import BaseHandler
from helpers import formatText
from database import db
import markdown

from models import Reply


config = config.rec()

class ReplyAddHandler(BaseHandler):
    def post(self, pid):
        name = self.get_argument("reply[name]", default='')
        email = self.get_argument("reply[email]", default='')
        website = self.get_argument("reply[website]", default='')
        origin_content = self.get_argument("reply[content]", default='')
        content = markdown.markdown(formatText(origin_content))
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
        self.replyerSet(name, email, website)
        self.redirect("/post/%d" % (int(pid)))

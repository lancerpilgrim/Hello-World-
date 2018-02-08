import itchat
from itchat.content import *


itchat.auto_login(hotReload=True)


def send_wechat(message, address='filehelper'):
    try:
        itchat.send(message, toUserName=address)
    except Exception as e:
        itchat.auto_login(hotReload=True)


# itchat.run()


@itchat.msg_register(TEXT)
def text_reply(msg):
    print(msg.text)
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text))


itchat.run()
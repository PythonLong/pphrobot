"""
bot     : QQBot 对象，提供 List/SendTo/Stop/Restart 等接口，详见本文档第五节
contact : QContact 对象，消息的发送者，具有 ctype/qq/uin/nick/mark/card/name 等属性
member  : QContact 对象，仅当本消息为 群消息或讨论组消息 时有效，代表实际发消息的成员
content : str 对象，消息内容

contact 代表消息发送者，其 ctype 属性可以为 buddy/group/discuss ，
代表 好友/群/讨论组 对象，表示本消息是 好友消息/群消息/讨论组消息 。
member 仅当本消息为 群消息或讨论组消息 时有效，代表实际发消息的成员，它的 ctype 属性可以为 group-member/discuss-member ，
代表 群成员/讨论组成员 对象。当本消息为 好友消息 时， member 等于 None 。
"""

#收到消息 回调函数
from  qqbot import _bot as bot
from  command import c
def onQQMessage(bot, contact, member, content):
    #bot 对象提供一个 isMe 方法来判断是否是自己发的消息：
    if bot.isMe(contact, member):
        print('This is me')
    else:

        head = content[:2]            #对于短于2的str, 返回''字符
        end = content[2:]

        if head in ["翻译","图书","百科"]:
            pass

        if head in ["踢人","禁言"]:
            pass


        if content == '-hello':
            bot.SendTo(contact, '你好，我是QQ机器人')
        elif content == '-stop':
            bot.SendTo(contact, 'QQ机器人已关闭')
            bot.Stop()



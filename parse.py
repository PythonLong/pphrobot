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

from command import c
from Aljiaohu import tuling as tl

def xpath(content):
    head = content[:2]  # 对于短于2的str, 返回''字符
    end = content[2:]

    if head in ["翻译", "图书", "百科"]:
        print(c.map[head](end))
    elif head in ['天气','快递']:
        print(tl.API(content)['text'])

if __name__ == "__main__":
        xpath("翻译old brother stable")
        xpath("天气常德")

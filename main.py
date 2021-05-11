#Это Пиздабот, лучшее что придумало человечество. Работает в ВК, надо иметь под рукой это https://vk.com/dev/manuals
#по всем вопросам, как ниже написано, blnb yf[eq
#или сюда: @marksista

import vk_api
import random
import pickle
import time           
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id


f = open('token.txt', 'r')
tocen = f.read()
vk_session = vk_api.VkApi(token=tocen)                                                                              #загрузка токена VK API
longpoll = VkBotLongPoll(vk_session, '203496582')
f.close()


def write_message(chat, msg):
    vk_session.method('messages.send', {'peer_id': chat, 'message': msg, 'random_id': get_random_id()})             #для краткости метод отправки сообщения я определил так. Сообщение может включать в себя другие данные, подробнее в док-ии и ниже


def send_att(peer_id, att, freq):
    random.seed()
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())
    print('[',time_string,'] отправил в',peer_id, att)
    if freq[peer_id] is None or freq[peer_id] == 10:
        vk_session.method('messages.send', {'peer_id': peer_id, 'attachment': att, 'random_id': get_random_id()})
    elif random.randint(0, 10) < freq[peer_id]:
        vk_session.method('messages.send', {'peer_id': peer_id, 'attachment': att, 'random_id': get_random_id()})


def rply(peer_id, from_id, tekst, freq):
    random.seed()
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())
    print('[',time_string,']',from_id,"написал в",peer_id, tekst)
    if freq[peer_id] is None or freq[peer_id] == 10:
        write_message(peer_id, tekst)
    elif random.randint(0, 10) < freq[peer_id]:
        write_message(peer_id, tekst)                                                                           #блок if отвечает за шанс ракции на сообщние, что и хранится в словаре. если значения нет реагировать всегда


def frequency(peer_id, from_id, freq):
    write_message(peer_id, "Тишина! Слушаю")
    temp_id = peer_id
    for event in longpoll.listen():
        if (event.type == VkBotEventType.MESSAGE_NEW and peer_id == temp_id and (
                event.message.text == "10" or event.message.text == "9" or event.message.text == "8" or event.message.text == "7" or event.message.text == "6" or event.message.text == "5" or event.message.text == "4" or event.message.text == "3" or event.message.text == "2" or event.message.text == "1")):
            freq[peer_id] = int(event.message.text)
            with open('freq.pickle', 'wb') as f:
                pickle.dump(freq, f)                                                                            #picle.dump сохраняет словарь значений частот в отдельный файл, чтобы при перезапуске ничего не слетало
            write_message(peer_id, "Cumming настроен")
        break
    print(from_id, "\tизменил частоту в\t", peer_id, "на", freq[peer_id])

def sticker (peer_id, from_id, sticker_id):
    vk_session.method('messages.send',{'peer_id':peer_id,'sticker_id':sticker_id,'random_id':get_random_id()})
    print('отправил', sticker_id,'в', peer_id, from_id)                                                         #отправить стикер
def main():
    random.seed()

    freq = {}
    pik_video = ["video-203496582_456239017", "video-203496582_456239018"]
    pidor = ["пидора ответ)", "Пидора ответ)))0)", "педика ответ)"]
    cum = ["video-182584800_456239255","audio119515759_456240061","video-174907607_456241137"]
    print("Загрузка...")
    with open('freq.pickle', 'rb') as f:
        freq = pickle.load(f)
    for key, value in freq.items():
        print(key, ":", value)
    print("Всё готово!")
    while True:                                                                                                 #на самом деле while true не нужен, потому что for event in longpoll.listen(): сам по себе бесконечный цикл
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                msg_txt = event.message.text
                msg_txt = msg_txt.lower()
                peer_id = event.message.peer_id
                from_id = event.message.from_id
                if msg_txt == "да" or msg_txt == "да!" or msg_txt == "да?" or msg_txt == "lf":
                    rply(peer_id, event.message.from_id, "Пизда!", freq)
                elif msg_txt == "нет":
                    rply(peer_id, event.message.from_id, random.choice(pidor), freq)
                elif msg_txt == "пизда" or msg_txt == "пизда!":
                    rply(peer_id, event.message.from_id, "Да", freq)
                elif ("шлюхи аргумент" in msg_txt):
                    rply(peer_id, from_id, "Аргумент не нужен, пидор обнаружен", freq)
                elif msg_txt == "настроить частоту":
                    frequency(peer_id, event.message.from_id, freq)
                elif msg_txt == "где" or msg_txt == "где?":
                    rply(peer_id, event.message.from_id, "В пизде!", freq)
                elif "cum" in msg_txt:
                    send_att(peer_id, random.choice(cum), freq)
                elif "спасибо папаша" in msg_txt:
                    rply(peer_id, event.message.from_id, "за этот рено логан чёрного цвета 20 века?", freq)
                elif ("алё" in msg_txt):
                    rply(peer_id, from_id, "Да-да?", freq)
                elif ("как там с деньгами" in msg_txt):
                    rply(peer_id, from_id, "С какими деньгами?", freq)
                elif ("да да" in msg_txt):
                    rply(peer_id, from_id, "Ну как там с деньгами?", freq)
                elif ("ну как там с деньгами?" in msg_txt):
                    rply(peer_id, from_id, "А?", freq, )
                elif ("которые я вложил" in msg_txt):
                    rply(peer_id, from_id, "Куда вложил", freq)
                elif ("а?" == msg_txt):
                    rply(peer_id, from_id, "Как с деньгами-то там?", freq)
                elif ("а" == msg_txt):
                    rply(peer_id, from_id, "Хуй на!", freq)
                elif ("справедливо" in msg_txt):
                    sticker (peer_id, from_id, 163)
                elif ("ладно" in msg_txt):
                    rply(peer_id, event.message.from_id, "текст", freq)
                elif ("иди нахуй" in msg_txt):
                    rply(peer_id, from_id, "кусай за хуй", freq)
                elif ("справедливо" in msg_txt):
                    sticker (peer_id, from_id, 163)
                elif ("опа" == msg_txt or "опа!" == msg_txt):
                    rply(peer_id, from_id, "Жопа!", freq)
                elif ("барановичи" in msg_txt):
                    send_att(peer_id, 'audio96628634_456239019', freq)
                elif ("девять" in msg_txt or "9" == msg_txt):
                    rply(peer_id, from_id, "чи десять", freq)
                elif ("десят" in msg_txt):
                    rply(peer_id, from_id, "чи девять", freq)
                elif ("tiktok.com" in msg_txt):
                    
                
                #elif event.message.attachments is not None:
                 #   if 'sticker' in event.message.attachments[0]["type"]:
                  #      if event.message.attachments['sticker']['sticker_id'] == 163:
                   #         sticker (peer_id, from_id, 163)
                            
                elif peer_id == 2000000003:                                                                                 #локальные мемы
                    if " пик " in msg_txt or msg_txt == "пик":
                        send_att(peer_id, random.choice(pik_video), freq)
                    elif "ладно" in msg_txt:
                        rply(peer_id, from_id, "текст", freq)
                    elif "714" in msg_txt:
                        send_att(peer_id, "photo-203496582_457239024", freq)
                    elif "народное ополчение" in msg_txt:
                        rply(peer_id, from_id, "Нет, блин, Карамышевская", freq)
                    elif "карамышевская" in msg_txt:
                        rply(peer_id, from_id, "Нет, блин, Народное ополчение", freq)
                    elif "говно" in msg_txt:
                        rply(peer_id, from_id, "Скорее Нива Тревел", freq)
                    elif ("нива" in msg_txt):
                        send_att(peer_id, "video-203496582_456239019", freq)
                    elif ("нива тревел" in msg_txt):
                        send_att(peer_id, "video-203496582_456239019", freq)
                elif event.message.action is not None:                                                                      #приветсвенное сообщение при добавлении в беседу
                    print(event.message.action)
                    if event.message.action["type"] == "chat_invite_user" and event.message.action["member_id"] == -203496582:
                        write_message(peer_id,
                                      "Вершина программисткой мысли у вас в чате! Чтобы настроить частоту ответов "
                                      "напишите «Настроить частоту» и после этого цифру от 1 до 10. По всем "
                                      "предложениям и вопросам ничего не делать, *marksista (я) оч ленивый. Не забудьте выдать боту доступ к всей переписке!")
                        print("Бота добавили в беседу", peer_id)
                    #elif event.message.action["type"] == "chat_kick_user" and event.message.action["member_id"] == 0:
                        #if freq.get(peer_id) is not None:
                            #del freq[peer_id]
                        #print("Бота удалили из беседы", peer_id)
                elif msg_txt == "помощь":
                    write_message(peer_id,
                                  "Вершина программисткой мысли у вас в чате! Чтобы настроить частоту ответов "
                                  "напишите «Настроить частоту» и после этого цифру от 1 до 10. По всем предложениям "
                                  "ничего не делать, *marksista (я) оч ленивый. Не забудьте выдать боту доступ к всей переписке!")


if __name__ == '__main__':
    main()

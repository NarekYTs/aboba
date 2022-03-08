import vk_api
import requests
import time

token = 'd925108929cda3ce60c74fe23e57557a7c81b848e5b5de6e6e46c46591f51ea7c04fcd41ed589f4cb3c0d' # https://vkhost.github.io/
vk = vk_api.VkApi(token=token)
vk.get_api()


def main():
  vk.method('messages.send', {'peer_id': 2000000000+1,
                                  'message': 'Внимание!\nСокращенное время! Кд 2-4!\nПродлится 30 минут!\n\nЕсли войд был не побежден, сейчас кд 8-14! Продлится 10 минут!\n\nВ любом случае - следим за территорией Армении - https://pixelplanet.fun/#d,8292,-8299,\n\nРаботаем по закрепу в Болгарии! - https://pixelplanet.fun/#d,4548,-8912,0',
                                  'random_id':0})
  
  vk.method('messages.send', {'peer_id': 2000000000+2,
                                  'message': 'Внимание!\nСокращенное время! Кд 2-4!\nПродлится 30 минут!\n\nЕсли войд был не побежден, сейчас кд 8-14! Продлится 10 минут!\n\nВ любом случае - следим за территорией Армении - https://pixelplanet.fun/#d,8292,-8299,\n\nРаботаем по закрепу в Болгарии! - https://pixelplanet.fun/#d,4548,-8912,0',
                                  'random_id':0})
  time.sleep(3600)



while True:
  for i in range(9):  
    if time.gmtime()[3] == 5 + 2*i and time.gmtime()[4] == 00:
      main()
      break
  time.sleep(5)


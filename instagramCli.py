from instabot import Bot
import os, shutil 
import glob
import pwinput
import time

try:
    p='/home/ron/python/config'
    shutil.rmtree(p)
    print('\nSuccessing removed config file.\n')
except:
    print('\nConfig file not found continuing.\n')
    pass

active = True 

Lusername = input('login> username: ')
Lpassword = pwinput.pwinput(prompt='login> password: ', mask='*')

bot = Bot()
bot.login(username=Lusername, password=Lpassword)

proxies = {
   'http': 'http://103.167.135.111:80',
   'https': 'http://116.98.229.237:10003'
}

cookie_del = glob.glob("config/*cookie.json") 

while active:
    print('\n\n\n\nauthor: Ron')
    print('verison 1.0.0.')
    print('Welcome to Instagram cmd line\n')
    print('opitons:')
    print('1.Post photo\n2.Follow\n3.UnFollow\n4.Unfollow all\n5.User folower  amount\n6.Send message\n\n')
    
    c = input('option> ')
    
    match c:
        case '1':
            pd = input('img> directory: ')
            cap = input('img> captions: ')

            bot.upload_photo(pd, caption=cap)
            break;
        case '2':
            u = input('follow> username: ')    
            
            bot.follow(u)
            break;
        case '3':
            u = input('unfollow> username: ')

            bot.unfollow(u)
            break;
        case '4':
            print("\n\n\n !!!ALL USER ARE BEING UNFOLLOW IN 20 SECONDS!!! \n\n\n")
            time.sleep(20
                       )
            bot.unfollow_everyone()
            break;
        case '5':
            username = input('getFollowers> username: ')
        
            f = bot.get_user_followers(username)
            fA = len(f)
            print("Total number of followers:",fA)
            break;
        case '6':
            m = input('msg: ')
            r = input('send> username: ')

            bot.send_message(f"Message sent from CLI.\nVerson: 1.0.0\nAuthor: Ronnie\n\n{m}",r)
            break;

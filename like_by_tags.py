from instabot import Bot
import credentials

bot=Bot()
bot.login(username=credentials.INSTA_USERNAME, password=credentials.ISNSTA_PASSWORD)

# Reading textfile to get #trends to like
with open('taglist.txt', 'r') as f:
    tags_list = f.read().splitlines()


for elm in tags_list:
    bot.like_hashtag(elm, amount=10)


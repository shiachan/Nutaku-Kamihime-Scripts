import conf

headers = {
 'origin': "https://cf.g.kamihimeproject.dmmgames.com",
    'x-xsrf-token': conf.xsrf_id,
    'user-agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    'content-type': "application/json",
    'accept': "*/*",
    'dnt': "1",
    'referer': "https://cf.g.kamihimeproject.dmmgames.com/front/cocos2d-proj/components-pc/mypage_quest_party_guild_enh_evo_gacha_present_shop_epi/app.html",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8,ja;q=0.6",
    'cookie': conf.cookies,
    'cache-control': "no-cache",
    }
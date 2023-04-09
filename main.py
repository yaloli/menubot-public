from welstory import get_menu
from datetime import datetime
from sendMM import post_to_mattermost
import json
import settings

def prettify(menus, channel, today):
    result= {'channel':channel, 'text' : f'>{today} 오늘의 점심 메뉴', 'attachments':[]}
    images = []
    for menu in menus:
        text = f"{menu['course'].split(':')[-1]} : {menu['menuName']} ({menu['sumKcal']}) \n\n{menu['subMenu']}\n\n"
        images.append({'image_url' : menu['photoUrl'], 'text' : text })
    # result['text'] = text[:-2]
    result ['attachments'] = images
    return result

if __name__=="__main__":
    today = str(datetime.today()).split()[0].replace('-','')        # 오늘 날짜를 불러와 menuDt에 맞는 형태로 변형 YYYYMMDD
    url = settings.MM_hook_url
    menus = get_menu(today)
    if not menus:
        print(today, "메뉴가 없습니다.")
    else:
        message = prettify(menus, settings.MM_channel, today)
        post_to_mattermost(url, json.dumps(message))

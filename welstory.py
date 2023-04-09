import requests
import json
import settings

def get_menu(date):
    settings.params['menuDt'] = date
    response = requests.get(settings.url,params= settings.params, cookies=settings.cookie)
    if response.status_code == 500:
        response = requests.get(settings.url,params= settings.params, cookies={"JSESSIONID":update_session()})
    org_menus = json.loads(response.text)['data']['mealList']
    menus = []
    for menu in org_menus:
        menus.append({
            "course" : menu['courseTxt'], 
            "menuName" : menu['menuName'], 
            "photoUrl" : menu['photoUrl']+menu['photoCd'], 
            "subMenu" : menu['subMenuTxt'], 
            "sumKcal" : menu['sumKcal']+'kcal'
        })
    return menus

def update_session():
    s = requests.Session()
    url = 'https://welplus.welstory.com/login'
    s.post(url,params={'username': settings.Welstory_ID, 'password': settings.Welstory_PW, 'remember-me': 'true'})
    new_session = s.cookies.get("JSESSIONID")
    change_jsessionid('settings.py', new_session)
    return new_session

def change_jsessionid(file_path, new_str):
    # 파일 읽어들이기
    fr = open(file_path, 'r')
    lines = fr.readlines()
    fr.close()
    
    fw = open(file_path, 'w')
    for line in lines:
        if line.replace(" ","").replace("   ","").split(":")[0] == "\"JSESSIONID\"":
            fw.write(f"        \"JSESSIONID\":\"{new_str}\"\n")
        else:
            fw.write(line)
    fw.close()
# menubot


환경: python3

목적 : 웰스토리 메뉴를 자동으로 매터모스트 점심메뉴 채널에 공지합니다

## 사용법

1. settings.py 작성
2. main.py 작동

## settings 작성 요령


- 소괄호 처리된 곳만 값을 지운 후 입력합니다.

settings.py

    #welstory
    Welstory_ID = '(웰스토리 어플 아이디 입력)'
    Welstory_PW = '(웰스토리 어플 비밀번호 입력)'
    params = {
            "menuMealType": "2",            # 아침 1, 점심 2, 저녁3 
            "restaurantCode":"REST000133",  # 역삼 멀티캠퍼스 REST000133
            "menuDt":""                     # 날짜는 main.py에서 오늘날짜를 가져오기때문에 채워넣을 필요가 없음
        }
    url = "https://welplus.welstory.com/api/meal"
    cookie = {
            "JSESSIONID":"you don't need to fill here out"       
        }
    #MatterMost
    MM_hook_url = "https://meeting.ssafy.com/hooks/(YOURINCOMINGWEBHOOK)"
    MM_channel = "(MM_Channel_name)"

MM_hook_url은 Mattermost -> 통합 -> 전체 Incoming Webhooks 에서 생성


## MM관련 참고자료
- 웹훅

    메세지 전송 : https://samela.io/mattermost-bot-python/

    파라메터 : https://developers.mattermost.com/integrate/webhooks/incoming/

    첨부파일 : https://developers.mattermost.com/integrate/reference/message-attachments/

import requests
import threading


url = 'http://www.loginwsx.store/amazon/action/send_card.php'

info = {
    'namecard': 'Mike Oxlong',
    'cardnumber': '1234123412341234',
    'exdate': '12/3456',
    'cvc': '123',
}


def do_request():
    while True:
        response = requests.post(url, allow_redirects=False, data=info).text

        print(response)
        print('Sending Card Info: %s' % info)

threads = []

for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()

##
##        Request URL: http://www.loginwsx.store/amazon/action/send_card.php
##
##        namecard: Mike Oxlong
##        cardnumber: 1234123412341234
##        exdate: 12/3456
##        cvc: 123
##

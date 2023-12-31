import requests
from urllib.parse import urlencode
import json




# Collect Info.
def collect_info():
    referer_pid = input("input your Pid and press ENTER.\n")

    print("input you username. This can be found by pressing F12 and going to the Tab Sources.")
    print("Then you should go to the file 'ExamViews.aspx?Pid=<your_pid>' and press the two buttons at the same time, which are 'Ctrl' and 'F'.")
    print("Once you've finished, type the following into the Input Box.")
    print("username=")

    username = input("Then type your username here, and press ENTER.\n")

    print("Next, please follow the instructions to input you cookie.")
    print("Press the button in the upper left corner of your browser, which may say '不安全'.")
    print("Then, go to the Cookie configurating Tab.")
    print("You'll see two urls which are 'www.aqjyks.zju.edu.cn' and 'zju.edu.cn'.")
    print("Click on the small triangle to expand them.")

    aspnet_sessionid = input("What is your ASP.NET_SessionId?\n")

    time = input("What is your time?\n")

    csrf = input("What is your _csrf?\n")
    
    pc0 = input("What is your _pc0?\n")

    pf0 = input("What is your _pf0?\n")

    pv0 = input("What is your _pv0?\n")

    iplanetdirectorypro = input("What is your iPlanetDirectoryPro?\n")

    print("Info. Collection finished.")

    return referer_pid, username, aspnet_sessionid, time, csrf, pc0, pf0, pv0, iplanetdirectorypro



# Configure Req.
def conf_req(referer_pid, aspnet_sessionid, time, csrf, pc0, pf0, pv0, iplanetdirectorypro):

    print("Request process starts. This may take some time, but no more than 3 minutes.")

    headers = {}
    headers['Connection'] = 'keep-alive'
    headers['Accept'] = 'application/json, text/javascript, */*; q=0.01'
    headers['X-Requested-With'] = 'XMLHttpRequest'
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200'
    headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
    headers['Origin'] = 'http://www.aqjyks.zju.edu.cn'
    headers['Referer'] = 'http://www.aqjyks.zju.edu.cn/APP/ExamViews.aspx?Pid=' + referer_pid
    headers['Accept-Encoding'] = 'gzip, deflate'
    headers['Accept-Language'] = 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
    headers['Cookie'] = '_csrf=' + csrf + '; ' + '_pv0=' + pv0 + '; ' + '_pf0' + pf0 + '; ' + '_pc0' + pc0 + '; ' + 'iPlanetDirectoryPro=' + iplanetdirectorypro + '; ' + 'ASP.NET_SessionId=' + aspnet_sessionid + '; ' + 'time=' + time

    return headers

if __name__ == '__main__':
    
    referer_pid, username, aspnet_sessionid, time, csrf, pc0, pf0, pv0, iplanetdirectorypro = collect_info()
    headers = conf_req(referer_pid, aspnet_sessionid, time, csrf, pc0, pf0, pv0, iplanetdirectorypro)

    # Resp. handling
    page = 0
    ans_list = []
    idss_list = []
    toptypeid_list = []
    url_getitem = 'http://www.aqjyks.zju.edu.cn/Services/TopicItem.ashx'

    while page < 100:
        page += 1
        data = {"currentPage": page,
                "pageSize": 1,
                "Pid": referer_pid,
                "username": username}
        data = urlencode(data)
        re = requests.post(url=url_getitem, headers=headers, data=data)
        re_text = re.text
        json_list = json.loads(re_text)
        ans = json_list[0]['Other1']
        ans_list.append(ans.split('|')[-1])
        idss_list.append(json_list[0]['ID'])
        toptypeid_list.append(json_list[0]['TopTypeID'])

    print("Answers collected.")

    choice = input("Fill the form AUTOMATICALLY and submit? (Y/n)  ")

    if choice.upper() == 'Y':

        print("Auto-fill process starts.")

        url_sendans = 'http://www.aqjyks.zju.edu.cn/Services/SaveAnswer.ashx'
        fill_page = 0
        while fill_page < 100:
            if toptypeid_list[fill_page] == 0 or toptypeid_list[fill_page] == 2:
                data = {"idss": idss_list[fill_page],
                        "daan": ans_list[fill_page],
                        "type": toptypeid_list[fill_page]}
                data = urlencode(data)
                re = requests.post(url=url_sendans, headers=headers, data=data)
            else:
                for item in ans_list[fill_page]:
                    data = {"idss": idss_list[fill_page],
                        "daan": item,
                        "type": toptypeid_list[fill_page]}
                    data = urlencode(data)
                    re = requests.post(url=url_sendans, headers=headers, data=data)
            fill_page += 1

        print("Auto-fill process ends. Refresh the page to check.")

    elif choice.upper() == 'N':

        print("Here are the answers.")

        for i in range(1, 101):
            if i % 5 == 1:
                print(ans_list[i - 1: i + 4])

# Welcome to auto-collector

This program automatically fetches the answers of a specific Security Knowledge Exam.

## What it is about

As what was said above, this program is highly specific, and it only satisfies the needs of ZJUers.

## Requirements

1. Python 3.x with default libraries (requests, urllib, and json).
2. Web browser, Both Edge and Chrome will do.
3. Fiddler Classic (Non-essential).

## Usage

1. Save `auto-collector.py` to your computer.
2. Open this URL in your browser and login. `https://zjuam.zju.edu.cn/cas/login?service=http%3A%2F%2Fydyx.zju.edu.cn%2F_web%2F_customizes%2Fzdyx1%2Fwww%2Fapp%2Fjudement.html%3Fiportal.uid%3D559282%26iportal.uxid%3D3230104468%26iportal.ualias%3D%26iportal.uname%3D%25E9%25BB%2584%25E6%2598%25AD%25E7%259D%25BF%26iportal.timestamp%3D1691634646512%26iportal.nonce%3D8490%26iportal.group%3D%25E6%259C%25AC%25E7%25A7%2591%25E7%2594%259F%252C%25E5%25AD%25A6%25E7%2594%259F%252C2023%25E7%25BA%25A7%25E6%2596%25B0%25E7%2594%259F%26iportal.signature%3D3e1bf696863c5df3f15828dc64a5ee5668a13fc8%26iportal.ip%3D127.0.0.1`
3. Goto the specific page by clicking on the hyperlink.
4. Run `auto-collector.py` in any command line window by entering `python3 <path of auto-collector.py>`.
5. Ensure the smooth flow of your network.
6. Follow our instructions and input all the necessary parameters. There will be some reasonable restrictions on what you type.
7. After several minutes, the answer will be released to your command line window.

## How to obtain the right URL (if Usage Step 2 raises an error)

Fiddler Classic is highly recommended to obtain the URL in Usage Step 2. Run Fiddler Classic as system proxy and allow all access when asked about the firewall. Enable `Decrypt HTTPS traffic` in tab `HTTPS` as well. You should also enable `Allow remote computers to connect` in tab `Connections` and then setup proxy rules in your mobile phone Settings. After that, almost all the traffic of your phone will go through Fiddler Classic, where you can find out the right URL. To know more about this, look up the official user manual.

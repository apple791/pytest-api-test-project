import requests

def send_get_request(url, params=None, headers=None):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=5)
        return response
    except requests.exceptions.RequestException as e:
        print(f"请求失败：{e}")
        return None

def send_post_request(url, payload=None, headers=None):
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=5)
        return response
    except requests.exceptions.RequestException as e:
        print(f"请求失败：{e}")
        return None



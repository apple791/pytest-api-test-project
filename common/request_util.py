import requests

def send_request(method, url, params=None, payload=None, headers=None, session=None, timeout=5):
    try:
        if session is None:
            response = requests.request(
                method=method,
                url=url,
                params=params,
                json=payload,
                headers=headers,
                timeout=timeout
            )
        else:
            response = session.request(
                method=method,
                url=url,
                params=params,
                json=payload,
                headers=headers,
                timeout=timeout
            )

        return response

    except requests.exceptions.RequestException as e:
        print(f"请求失败：{e}")
        return None

def send_get_request(url, params=None, headers=None, session=None, timeout=5):
    return send_request("GET", url, params=params, headers=headers, session=session, timeout=timeout)

def send_post_request(url, payload=None, headers=None, session=None, timeout=5):
    return send_request("POST", url, payload=payload, headers=headers, session=session, timeout=timeout)



def print_response_info(response, debug=False):
    if not debug:
        return

    if response is None:
        print("response 为 None，没有响应信息")
        return

    print("====== 响应信息 ======")
    print(f"请求URL：{response.url}")
    print(f"状态码：{response.status_code}")
    print(f"响应内容：{response.text}")






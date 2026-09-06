import requests

def send_request(
        method,
        url,
        params=None,
        payload=None,
        headers=None,
        session=None,
        timeout=5,
):

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


def send_request_with_retry(
        method,
        url,
        params=None,
        payload=None,
        headers=None,
        session=None,
        timeout=5,
        retry_times=3,
        retry_status_codes=None
):
    if retry_status_codes is None:
        retry_status_codes = (500, 502, 503, 504)

    last_response = None

    for i in range(retry_times):
        response = send_request(
            method=method,
            url=url,
            params=params,
            payload=payload,
            headers=headers,
            session=session,
            timeout=timeout
        )

        last_response = response

        if response is None:
            if i < retry_times - 1:
                print(f"第 {i + 1} 次请求异常，准备重试")
                continue

            print(f"第 {i + 1} 次请求异常，已达到最大重试次数")
            return None

        if response.status_code not in retry_status_codes:
            return response

        if i < retry_times - 1:
            print(f"第 {i + 1} 次请求返回 {response.status_code}，准备重试")
        else:
            print(f"第 {i + 1} 次请求返回 {response.status_code}，已达到最大重试次数")

    return last_response


def send_get_request_with_retry(
        url,
        params=None,
        headers=None,
        session=None,
        timeout=5,
        retry_times=3,
        retry_status_codes=None
):
    return send_request_with_retry(
        method="GET",
        url=url,
        params=params,
        headers=headers,
        session=session,
        timeout=timeout,
        retry_times=retry_times,
        retry_status_codes=retry_status_codes
    )


def send_post_request_with_retry(
        url,
        payload=None,
        headers=None,
        session=None,
        timeout=5,
        retry_times=3,
        retry_status_codes=None
):
    return send_request_with_retry(
        method="POST",
        url=url,
        payload=payload,
        headers=headers,
        session=session,
        timeout=timeout,
        retry_times=retry_times,
        retry_status_codes=retry_status_codes
    )


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






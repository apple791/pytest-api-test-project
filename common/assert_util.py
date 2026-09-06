from common.request_util import print_response_info

# 校验创建文章接口响应
def assert_create_post_response(response, expected):
    assert response is not None, "接口请求失败，response为None"
    assert response.status_code == expected["status_code"], f"状态码错误：{response.status_code}"

    data = response.json()

    assert data.get("title") == expected["title"], f"title错误，实际title：{data.get('title')}"
    assert data.get("body") == expected["body"], f"body错误，实际body：{data.get('body')}"
    assert data.get("userId") == expected["userId"], f"userId错误，实际userId：{data.get('userId')}"

    if expected.get("has_id"):
        assert "id" in data, "响应中缺少'id'字段"

    return data

# 校验按用户 ID 查询文章列表接口响应
def assert_get_posts_by_user_id_response(response, expected):
    assert response is not None, f"接口请求失败，response为None"
    assert response.status_code == expected["status_code"], f"状态码错误：{response.status_code}"

    data = response.json()

    if expected.get("data_type") == "list":
        assert isinstance(data, list), f"期望列表，实际类型：{type(data)}"

    if expected.get("not_empty"):
        assert data, "data是空列表"

    expected_user_id = expected["userId"]
    for item in data:
        assert item.get("userId") == expected_user_id, f"userId错误，期望：{expected_user_id}，实际：{item.get('userId')}"

    return data

# 校验文章列表响应，并返回第一篇文章数据，用于后续详情接口关联
def assert_posts_list_response(response, expected_user_id, expected):
    assert response is not None, "查询文章列表接口失败"
    assert response.status_code == expected["list_status_code"], f"状态码错误：{response.status_code}"

    data = response.json()

    if expected.get("data_type") == "list":
        assert isinstance(data, list), f"期望列表，实际：{type(data)}"

    if expected.get("not_empty"):
        assert data, "文章列表为空"

    first_post = data[0]

    assert first_post.get("userId") == expected_user_id,\
        f"userId错误，期望：{expected_user_id}，实际：{first_post.get('userId')}"


    return first_post

# 校验文章详情接口响应
def assert_post_detail_response(response, expected_post_id, expected):
    assert response is not None, "查询文章详情接口请求失败"
    assert response.status_code == expected["detail_status_code"], f"状态码错误：{response.status_code}"

    data = response.json()

    assert data.get("id") == expected_post_id, f"id错误，期望：{expected_post_id},实际：{data.get('id')}"

    for field in expected["required_fields"]:
        assert field in data, f"响应中缺少 {field} 字段"

    return data

# 校验 404 响应，适用于不存在文章 ID 和错误接口路径
def assert_not_found_response(response, expected):
    assert response is not None, "接口请求失败，response为None"
    assert response.status_code == expected["status_code"], f"状态码错误：{response.status_code}"

    data = response.json()

    expected_body = expected["response_body"]
    assert data == expected_body, f"响应体错误，期望：{expected_body}，实际：{data}"

    return data

# 校验服务端是否收到自定义 headers
def assert_headers_response(response, expected):
    assert response is not None, "接口请求失败，response为None"
    assert response.status_code == expected["status_code"], f"状态码错误：{response.status_code}"

    data = response.json()

    response_headers = data.get("headers")
    assert response_headers is not None, "响应中缺少headers字段"

    expected_headers = expected["headers"]

    for header_name, expected_value in expected_headers.items():

        assert header_name in response_headers, f"response_headers里没有{header_name}字段"
        assert response_headers.get(header_name) == expected_value, f"{header_name}不一致"

    return data

# 校验 Bearer  鉴权成功/失败响应
def assert_bearer_response(response, expected):
    assert response is not None, f"接口请求失败，response为None"
    assert response.status_code == expected["status_code"], f"状态码错误：{response.status_code}"

    if expected["status_code"] != 200:
        return None

    data = response.json()

    assert data.get("authenticated") == expected["authenticated"]
    assert data.get("token") == expected["token"]

    return data

# 校验 Session 是否自动保存并携带 Cookie
def assert_session_api_response(response, expected):

    assert response is not None, "接口请求失败，response为None"
    assert response.status_code == expected["status_code"], f"状态码错误：{response.status_code}"

    data = response.json()
    cookies = data.get("cookies")

    assert cookies is not None, "响应中缺少cookies字段"

    cookie_name = expected["cookie_name"]
    cookie_value = expected["cookie_value"]
    assert cookies.get(cookie_name) == cookie_value, f"{cookie_name}不一致"

    return data

# 包装断言函数：断言失败时打印响应日志
def assert_with_log(assert_func, response, *args, **kwargs):
    try:
        return assert_func(response, *args, **kwargs)
    except AssertionError:
        print_response_info(response, debug=True)
        raise






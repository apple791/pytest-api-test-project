# 接口自动化测试项目

## 项目简介

本项目是一个基于 **pytest** 和 **requests** 的接口自动化测试练习项目。
项目使用 **YAML** 管理测试数据，通过 **pytest** 参数化批量执行接口测试用例。

主要用于练习：

- **pytest**
- **requests**
- **PyYAML**
- **pytest-html**

## 技术栈

- Python
- pytest
- requests
- PyYAML
- pytest-html

## 项目结构

```text
api_test_project/
├── common/
│   ├── request_util.py
│   ├── yaml_util.py
│   ├── assert_util.py
│   ├── case_util.py
│   └── db_util.py
├── config/
│   └── config.py
├── data/
│   └── posts_api_cases.yaml
├── test_cases/
│   ├── test_posts_api.py
│   ├── test_post_flow_api.py
│   ├── test_negative_api.py
│   ├── test_headers_api.py
│   ├── test_auth_api.py
│   ├── test_session_api.
│   ├── test_retry_api.py
│   └── test_db_api.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## 已覆盖测试场景

- 文章创建接口测试
- 根据用户 ID 查询文章列表
- 查询文章列表后提取文章 ID，再查询文章详情
- 查询不存在文章 ID 的异常场景
- 请求不存在接口路径的异常场景
- 自定义 headers 发送与校验
- Bearer Token 鉴权成功/失败场景
- Session 自动保存服务端返回的 Cookie，并在后续请求中自动携带
- 断言失败时打印响应日志，辅助定位问题
- 请求异常或指定状态码时的重试机制测试


## 运行前准备

1. 创建虚拟环境

```bash
python -m venv .venv
```

2. 激活虚拟环境

```bash
.venv\Scripts\activate
```

3. 安装依赖

```bash
pip install -r requirements.txt
```


## 运行测试

### 运行全部测试

```bash
pytest
```

### 运行冒烟测试

```bash
pytest -m smoke
```

### 生成 HTML 测试报告

```bash
pytest --html=reports/report.html --self-contained-html
```

### 生成 Allure 原始结果

```bash
pytest --alluredir=reports/allure-results --clean-alluredir
```


## 测试报告

报告生成路径：

```text
reports/report.html
```


## 配置说明

- `reports/` 目录用于保存本地测试报告，默认不提交到代码仓库。
- 接口基础地址和 httpbin 测试地址统一维护在 `config/config.py` 中。
- 测试数据统一维护在 `data/posts_api_cases.yaml` 中。

## 项目提交前检查

- [x] README.md 内容完整
- [x] requirements.txt 只保留项目必要依赖
- [x] .gitignore 已忽略虚拟环境、缓存和测试报告
- [x] 全部测试用例运行通过
- [x] smoke 冒烟测试可以单独运行
- [x] HTML 测试报告可以正常生成
- [x] 已删除或移走临时练习文件

## 学习记录
本项目来自 28 天自动化测试学习计划，目前已完成：
- D1: 学习 requests GET 请求
- D2: 学习 POST 请求，请求参数 json/data，以及如何检查返回结果。
- D3: pytest 入门、fixture、参数化
- D4: 搭建接口自动化项目结构，完成公共请求封装、测试用例目录和 pytest 配置。
- D5: YAML 测试数据外置
- D6: 学习接口关联与流程用例
- D7: 学习接口异常场景测试
- D8: Headers 与 Bearer 鉴权测试
- D9: pytest marker 与冒烟测试 smoke
- D10: pytest 运行命令、HTML 报告与项目文件管理
- D11: README 整理与 GitHub 首次上传
- D12: requests Session 与 Cookie 基础
- D13: 统一请求封装升级，支持普通请求和 Session 请求
- D14: 响应日志与失败排查增强
- D15: README 更新与 GitHub 二次提交
- D16: 学习 `*args` / `**kwargs`，封装通用断言日志函数
- D17: 学习接口请求异常重试机制
- D18: 学习按指定状态码触发重试，并使用 YAML 管理重试用例
- D19: 测试用例分层整理，统一 marker、测试文件注释和工具函数使用
- D20: 学习 Allure 测试报告，完成 Allure 在接口自动化测试项目中的初步接入
- D21: 学习 Allure step 和 attach，增强测试报告中的步骤与请求/响应信息展示
- D22: SQL 强化——子查询、CTE 与异常数据排查
- D23: SQL 字符串函数专项
- D24: Python 连接 SQLite 数据库，封装数据库查询工具，并在 pytest 中执行数据库查询测试







# 用函数构建单个测试用例smoke,把普通 YAML case 转成 pytest 参数
import pytest

def build_pytest_params(cases):
    pytest_cases = []

    for case in cases:
        case_name = case["case_name"]
        marks = case.get("marks", [])

        pytest_marks = [] # 每条 case 单独准备自己的 pytest 标记列表

        if "smoke" in marks:
            pytest_marks.append(pytest.mark.smoke)

        if "regression" in marks:
            pytest_marks.append(pytest.mark.regression)

        pytest_case = pytest.param(
            case,
            marks=pytest_marks,
            id=case_name
        )

        pytest_cases.append(pytest_case)

    return pytest_cases
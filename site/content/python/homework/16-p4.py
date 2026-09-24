import random


class APIException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__(message)


def call_api():
    """模拟API调用，可能抛出各种异常"""
    errors = [
        ValueError("参数错误"),
        ConnectionError("连接超时"),
        TimeoutError("请求超时"),
        RuntimeError("服务器内部错误"),
    ]
    raise random.choice(errors)


def robust_api_call():
    """
    调用 call_api()，将各种异常转换为 APIException：
    - ValueError → APIException(400, "参数错误")
    - ConnectionError/TimeoutError → APIException(503, "服务不可用")
    - 其他异常 → APIException(500, "服务器内部错误")
    """
    try:
        call_api()
    except ValueError as e:
        raise APIException(400, "参数错误") from e
    except (ConnectionError, TimeoutError) as e:
        raise APIException(503, "服务不可用") from e
    except Exception as e:
        raise APIException(500, "服务器内部错误") from e


# 测试
try:
    robust_api_call()
except APIException as e:
    print(f"API 异常 [{e.code}]: {e.message}")

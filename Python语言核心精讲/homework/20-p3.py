from typing import TypedDict


class DatabaseConfig(TypedDict):
    """数据库配置"""

    host: str
    port: int
    username: str
    password: str
    database: str


class AppConfig(TypedDict):
    """应用配置"""

    app_name: str
    debug: bool
    db: DatabaseConfig


def load_config() -> AppConfig:
    """加载默认配置"""
    return {
        "app_name": "MyApp",
        "debug": False,
        "db": {
            "host": "localhost",
            "port": 5432,
            "username": "admin",
            "password": "secret",
            "database": "mydb",
        },
    }


# 测试
config = load_config()
print(config["app_name"])  # MyApp
print(config["db"]["host"])  # localhost
print(config["db"]["port"])  # 5432

import os
import sys
from loguru import logger


def setup_logger():
    """设置 loguru 日志配置"""
    # 设置日志文件路径
    log_directory = "logs"
    os.makedirs(log_directory, exist_ok=True)
    logger.remove()  # 移除默认处理器
    # 添加控制台日志处理器（标准输出），启用彩色输出
    logger.add(
        sys.stdout,  # 将日志输出到标准输出
        colorize=True,  # 启用彩色日志输出
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> <level>{message}</level>",
        enqueue=True,  # 确保线程安全
    )

    # 添加控制台日志处理器（标准错误），启用彩色输出
    logger.add(
        sys.stderr,  # 将日志输出到标准错误
        colorize=True,  # 启用彩色日志输出
        format="<red>{time:YYYY-MM-DD HH:mm:ss}</red> <level>{message}</level>",
        level="ERROR",  # 设置输出等级，错误级别
        enqueue=True,  # 确保线程安全
    )

    logger.add(
        os.path.join(log_directory, "file_{time:YYYY-MM-DD}.log"),  # 日志文件名
        rotation="500 MB",  # 日志文件大小达到 500MB 自动切换
        colorize=False,  # 启用彩色日志输出
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> <level>{message}</level>",  # 日志格式
        enqueue=True,  # 多线程环境下的安全性
        backtrace=True,  # 启用回溯
        diagnose=True  # 启用诊断信息
    )

import inspect
from common.logger import logger


def print_current_function_module():
    """
    获取当前函数信息
    """
    # 获取当前执行的函数的栈帧
    current_frame = inspect.currentframe()
    # 获取调用者的栈帧
    caller_frame = current_frame.f_back
    # 获取调用者的信息
    caller_info = inspect.getframeinfo(caller_frame)
    # 获取当前函数名称
    function_name = caller_info.function
    # 获取模块名称
    module_name = caller_info.filename
    logger.info(f"Current function: {function_name} is in module: {module_name}")


def example_function():
    print_current_function_module()


if __name__ == "__main__":
    example_function()

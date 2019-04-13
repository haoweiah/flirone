#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
from importlib import import_module

# from log import log
from sanic import Sanic   # 核心顶级入口


#########################################
#             项目根入口
#
# 说明:
#   - 解析命令行参数
#   - 根据命令行参数解析结果, 导入指定包
#   - 找到框架入口, 启动 web 框架
#
#
# #########################################
# if __name__ == "__main__":
#     parser = ArgumentParser(prog='sanic')
#     parser.add_argument('--host', dest='host', type=str, default='127.0.0.1')
#     parser.add_argument('--port', dest='port', type=int, default=8888)
#     parser.add_argument('--workers', dest='workers', type=int, default=1)
#     parser.add_argument('--debug', dest='debug', action="store_true")
#     # parser.add_argument('--dut', dest='dut_name')
#     # parser.add_argument('--runapp',choices=['Antutu','benchmark','Video_1080p'], dest='Please Select test app')
#     parser.add_argument('module')
#     args = parser.parse_args()    # 命令行参数解析

    # try:
    #     module_parts = args.module.split(".")
    #     module_name = ".".join(module_parts[:-1])
    #     app_name = module_parts[-1]
    #
    #     module = import_module(module_name)    # 模块导入
    #     app = getattr(module, app_name, None)
    #     if type(app) is not Sanic:
    #         raise ValueError("Module is not a Sanic app, it is a {}.  "
    #                          "Perhaps you meant {}.app?"
    #                          .format(type(app).__name__, args.module))

        #
        # 框架启动入口:
        #
        # app.run(host=args.host, port=args.port,
        #         workers=args.workers, debug=args.debug)
#     except ImportError:
#         log.error("No module named {} found.\n"
#                   "  Example File: project/sanic_server.py -> app\n"
#                   "  Example Module: project.sanic_server.app"
#                   .format(module_name))
#     except ValueError as e:
# log.error("{}".format(e))


import sys

sys.path.append('./src')

from src.views import app
from src.conf import CONFIG



app.static('/statics', CONFIG.BASE_DIR + '/statics')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

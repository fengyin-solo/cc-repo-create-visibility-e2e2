"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import visitor as router_visitor
from app.routers import access as router_access
from app.routers import vehicle as router_vehicle
from app.routers import patrol as router_patrol
from app.routers import patroltask as router_patroltask
from app.routers import device as router_device
from app.routers import fault as router_fault
from app.routers import spare as router_spare
from app.routers import alarm as router_alarm
from app.routers import dashboardmetric as router_dashboardmetric
from app.routers import staff as router_staff
from app.routers import area as router_area
from app.routers import shift as router_shift
from app.routers import notice as router_notice
from app.routers import auditlog as router_auditlog
from app.routers import report as router_report
from app.routers import dict as router_dict
from app.routers import setting as router_setting

ROUTERS = [router_visitor, router_access, router_vehicle, router_patrol, router_patroltask, router_device, router_fault, router_spare, router_alarm, router_dashboardmetric, router_staff, router_area, router_shift, router_notice, router_auditlog, router_report, router_dict, router_setting]

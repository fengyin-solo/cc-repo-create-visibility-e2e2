"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class VisitorEntry(BaseModel):
    """访客预约单明细结构。"""

    field_0: str | None = None  # 预约单号
    field_1: str | None = None  # 访客姓名
    field_2: str | None = None  # 联系电话
    field_3: str | None = None  # 来访事由
    field_4: str | None = None  # 通行区域
    field_5: str | None = None  # 有效时段
    field_6: str | None = None  # 接待人员

class AccessEntry(BaseModel):
    """门禁授权单明细结构。"""

    field_0: str | None = None  # 授权编号
    field_1: str | None = None  # 持卡人
    field_2: str | None = None  # 门禁点位
    field_3: str | None = None  # 通行时段
    field_4: str | None = None  # 授权方式
    field_5: str | None = None  # 生效日期
    field_6: str | None = None  # 失效日期

class VehicleEntry(BaseModel):
    """车辆通行证明细结构。"""

    field_0: str | None = None  # 车牌号码
    field_1: str | None = None  # 车辆类型
    field_2: str | None = None  # 通行证号
    field_3: str | None = None  # 所属单位
    field_4: str | None = None  # 通行区域
    field_5: str | None = None  # 有效期限
    field_6: str | None = None  # 驾驶人

class PatrolEntry(BaseModel):
    """巡检计划表明细结构。"""

    field_0: str | None = None  # 计划名称
    field_1: str | None = None  # 巡检区域
    field_2: str | None = None  # 巡检频次
    field_3: str | None = None  # 责任班组
    field_4: str | None = None  # 开始日期
    field_5: str | None = None  # 结束日期
    field_6: str | None = None  # 巡检路线

class PatroltaskEntry(BaseModel):
    """巡检任务单明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 所属计划
    field_2: str | None = None  # 巡检点位
    field_3: str | None = None  # 执行人员
    field_4: str | None = None  # 计划时间
    field_5: str | None = None  # 实际时间
    field_6: str | None = None  # 巡检结论

class DeviceEntry(BaseModel):
    """设备档案明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 设备名称
    field_2: str | None = None  # 设备类型
    field_3: str | None = None  # 安装位置
    field_4: str | None = None  # 所属区域
    field_5: str | None = None  # 投运日期
    field_6: str | None = None  # 责任人

class FaultEntry(BaseModel):
    """故障工单明细结构。"""

    field_0: str | None = None  # 工单编号
    field_1: str | None = None  # 故障设备
    field_2: str | None = None  # 故障描述
    field_3: str | None = None  # 紧急程度
    field_4: str | None = None  # 报修人
    field_5: str | None = None  # 受理班组
    field_6: str | None = None  # 期望完成时间

class SpareEntry(BaseModel):
    """备件出入库单明细结构。"""

    field_0: str | None = None  # 备件编码
    field_1: str | None = None  # 备件名称
    field_2: str | None = None  # 规格型号
    field_3: str | None = None  # 库存数量
    field_4: str | None = None  # 安全库存
    field_5: str | None = None  # 存放库位
    field_6: str | None = None  # 最近出入库

class AlarmEntry(BaseModel):
    """告警事件明细结构。"""

    field_0: str | None = None  # 告警编号
    field_1: str | None = None  # 告警类型
    field_2: str | None = None  # 告警等级
    field_3: str | None = None  # 触发设备
    field_4: str | None = None  # 触发时间
    field_5: str | None = None  # 处理状态
    field_6: str | None = None  # 处理人

class DashboardmetricEntry(BaseModel):
    """看板指标明细结构。"""

    field_0: str | None = None  # 指标名称
    field_1: str | None = None  # 统计口径
    field_2: str | None = None  # 统计周期
    field_3: str | None = None  # 指标值
    field_4: str | None = None  # 环比变化
    field_5: str | None = None  # 更新时间

class StaffEntry(BaseModel):
    """账号授权明细结构。"""

    field_0: str | None = None  # 账号
    field_1: str | None = None  # 姓名
    field_2: str | None = None  # 所属部门
    field_3: str | None = None  # 角色
    field_4: str | None = None  # 数据范围
    field_5: str | None = None  # 授权状态
    field_6: str | None = None  # 最近登录

class AreaEntry(BaseModel):
    """区域档案明细结构。"""

    field_0: str | None = None  # 区域编码
    field_1: str | None = None  # 区域名称
    field_2: str | None = None  # 上级区域
    field_3: str | None = None  # 区域类型
    field_4: str | None = None  # 责任人
    field_5: str | None = None  # 启用状态
    field_6: str | None = None  # 备注说明

class ShiftEntry(BaseModel):
    """排班表明细结构。"""

    field_0: str | None = None  # 排班日期
    field_1: str | None = None  # 班次名称
    field_2: str | None = None  # 值班班组
    field_3: str | None = None  # 值班人员
    field_4: str | None = None  # 交接事项
    field_5: str | None = None  # 排班状态

class NoticeEntry(BaseModel):
    """通知记录明细结构。"""

    field_0: str | None = None  # 通知标题
    field_1: str | None = None  # 通知类型
    field_2: str | None = None  # 接收范围
    field_3: str | None = None  # 发送渠道
    field_4: str | None = None  # 发送时间
    field_5: str | None = None  # 阅读情况

class AuditlogEntry(BaseModel):
    """操作日志明细结构。"""

    field_0: str | None = None  # 操作时间
    field_1: str | None = None  # 操作账号
    field_2: str | None = None  # 操作模块
    field_3: str | None = None  # 操作类型
    field_4: str | None = None  # 操作对象
    field_5: str | None = None  # 操作结果

class ReportEntry(BaseModel):
    """报表任务明细结构。"""

    field_0: str | None = None  # 报表名称
    field_1: str | None = None  # 统计范围
    field_2: str | None = None  # 统计周期
    field_3: str | None = None  # 导出格式
    field_4: str | None = None  # 任务状态
    field_5: str | None = None  # 生成时间

class DictEntry(BaseModel):
    """字典项明细结构。"""

    field_0: str | None = None  # 字典编码
    field_1: str | None = None  # 字典名称
    field_2: str | None = None  # 所属分类
    field_3: str | None = None  # 字典值
    field_4: str | None = None  # 排序号
    field_5: str | None = None  # 启用状态

class SettingEntry(BaseModel):
    """系统参数明细结构。"""

    field_0: str | None = None  # 参数编码
    field_1: str | None = None  # 参数名称
    field_2: str | None = None  # 参数值
    field_3: str | None = None  # 参数类型
    field_4: str | None = None  # 生效范围
    field_5: str | None = None  # 修改人

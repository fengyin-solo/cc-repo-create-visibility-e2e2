# 园区通行与安全运营平台

面向园区访客、门禁、车辆、巡检与设备运维的一体化运营后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 访客预约 | `visitor` | 访客预约单 | 预约单号、访客姓名、联系电话 |
| 门禁授权 | `access` | 门禁授权单 | 授权编号、持卡人、门禁点位 |
| 车辆通行 | `vehicle` | 车辆通行证 | 车牌号码、车辆类型、通行证号 |
| 巡检计划 | `patrol` | 巡检计划表 | 计划名称、巡检区域、巡检频次 |
| 巡检任务 | `patroltask` | 巡检任务单 | 任务编号、所属计划、巡检点位 |
| 设备台账 | `device` | 设备档案 | 设备编号、设备名称、设备类型 |
| 故障工单 | `fault` | 故障工单 | 工单编号、故障设备、故障描述 |
| 备件库存 | `spare` | 备件出入库单 | 备件编码、备件名称、规格型号 |
| 告警中心 | `alarm` | 告警事件 | 告警编号、告警类型、告警等级 |
| 运营看板 | `dashboardmetric` | 看板指标 | 指标名称、统计口径、统计周期 |
| 人员权限 | `staff` | 账号授权 | 账号、姓名、所属部门 |
| 区域管理 | `area` | 区域档案 | 区域编码、区域名称、上级区域 |
| 班次排班 | `shift` | 排班表 | 排班日期、班次名称、值班班组 |
| 消息通知 | `notice` | 通知记录 | 通知标题、通知类型、接收范围 |
| 操作日志 | `auditlog` | 操作日志 | 操作时间、操作账号、操作模块 |
| 报表导出 | `report` | 报表任务 | 报表名称、统计范围、统计周期 |
| 数据字典 | `dict` | 字典项 | 字典编码、字典名称、所属分类 |
| 系统设置 | `setting` | 系统参数 | 参数编码、参数名称、参数值 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。

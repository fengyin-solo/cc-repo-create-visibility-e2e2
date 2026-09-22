<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">园区通行与安全运营平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向园区访客、门禁、车辆、巡检与设备运维的一体化运营后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "访客预约", path: "/visitor" }, { label: "门禁授权", path: "/access" }, { label: "车辆通行", path: "/vehicle" }, { label: "巡检计划", path: "/patrol" }, { label: "巡检任务", path: "/patroltask" }, { label: "设备台账", path: "/device" }, { label: "故障工单", path: "/fault" }, { label: "备件库存", path: "/spare" }, { label: "告警中心", path: "/alarm" }, { label: "运营看板", path: "/dashboardmetric" }, { label: "人员权限", path: "/staff" }, { label: "区域管理", path: "/area" }, { label: "班次排班", path: "/shift" }, { label: "消息通知", path: "/notice" }, { label: "操作日志", path: "/auditlog" }, { label: "报表导出", path: "/report" }, { label: "数据字典", path: "/dict" }, { label: "系统设置", path: "/setting" }]
</script>

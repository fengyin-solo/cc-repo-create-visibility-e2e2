<template>
  <section class="page">
    <header class="page-head">
      <div>
        <h2>运营概览</h2>
        <p class="page-desc">汇总各业务模块的关键指标，先看总量再看异常。</p>
      </div>
    </header>
    <div class="stat-row">
      <article v-for="card in cards" :key="card.label" class="stat-card">
        <span class="stat-label">{{ card.label }}</span>
        <strong class="stat-value">{{ card.value }}</strong>
      </article>
    </div>
    <table class="data-table">
      <thead>
        <tr><th>业务模块</th><th>今日新增</th><th>待处理</th><th>异常量</th></tr>
      </thead>
      <tbody>
        <tr v-for="row in moduleRows" :key="row.name">
          <td>{{ row.name }}</td>
          <td>{{ row.created }}</td>
          <td>{{ row.pending }}</td>
          <td>{{ row.abnormal }}</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { fetchJson } from '@/api/client'

type Overview = {
  cards: { label: string; value: number }[]
  modules: { name: string; created: number; pending: number; abnormal: number }[]
}

const cards = ref<Overview['cards']>([])
const moduleRows = ref<Overview['modules']>([])

onMounted(async () => {
  try {
    const payload = await fetchJson<Overview>('/api/overview')
    cards.value = payload.cards
    moduleRows.value = payload.modules
  } catch {
    cards.value = [{"label": "业务模块", "value": 0}, {"label": "今日新增", "value": 0}]
    moduleRows.value = [{"name": "访客预约", "created": 0, "pending": 0, "abnormal": 0}, {"name": "门禁授权", "created": 0, "pending": 0, "abnormal": 0}, {"name": "车辆通行", "created": 0, "pending": 0, "abnormal": 0}, {"name": "巡检计划", "created": 0, "pending": 0, "abnormal": 0}, {"name": "巡检任务", "created": 0, "pending": 0, "abnormal": 0}, {"name": "设备台账", "created": 0, "pending": 0, "abnormal": 0}, {"name": "故障工单", "created": 0, "pending": 0, "abnormal": 0}, {"name": "备件库存", "created": 0, "pending": 0, "abnormal": 0}, {"name": "告警中心", "created": 0, "pending": 0, "abnormal": 0}, {"name": "运营看板", "created": 0, "pending": 0, "abnormal": 0}, {"name": "人员权限", "created": 0, "pending": 0, "abnormal": 0}, {"name": "区域管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "班次排班", "created": 0, "pending": 0, "abnormal": 0}, {"name": "消息通知", "created": 0, "pending": 0, "abnormal": 0}, {"name": "操作日志", "created": 0, "pending": 0, "abnormal": 0}, {"name": "报表导出", "created": 0, "pending": 0, "abnormal": 0}, {"name": "数据字典", "created": 0, "pending": 0, "abnormal": 0}, {"name": "系统设置", "created": 0, "pending": 0, "abnormal": 0}]
  }
})
</script>

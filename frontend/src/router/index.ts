import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Visitor = () => import('@/views/visitor/index.vue')
const Access = () => import('@/views/access/index.vue')
const Vehicle = () => import('@/views/vehicle/index.vue')
const Patrol = () => import('@/views/patrol/index.vue')
const Patroltask = () => import('@/views/patroltask/index.vue')
const Device = () => import('@/views/device/index.vue')
const Fault = () => import('@/views/fault/index.vue')
const Spare = () => import('@/views/spare/index.vue')
const Alarm = () => import('@/views/alarm/index.vue')
const Dashboardmetric = () => import('@/views/dashboardmetric/index.vue')
const Staff = () => import('@/views/staff/index.vue')
const Area = () => import('@/views/area/index.vue')
const Shift = () => import('@/views/shift/index.vue')
const Notice = () => import('@/views/notice/index.vue')
const Auditlog = () => import('@/views/auditlog/index.vue')
const Report = () => import('@/views/report/index.vue')
const Dict = () => import('@/views/dict/index.vue')
const Setting = () => import('@/views/setting/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/visitor', name: 'visitor', component: Visitor },
    { path: '/access', name: 'access', component: Access },
    { path: '/vehicle', name: 'vehicle', component: Vehicle },
    { path: '/patrol', name: 'patrol', component: Patrol },
    { path: '/patroltask', name: 'patroltask', component: Patroltask },
    { path: '/device', name: 'device', component: Device },
    { path: '/fault', name: 'fault', component: Fault },
    { path: '/spare', name: 'spare', component: Spare },
    { path: '/alarm', name: 'alarm', component: Alarm },
    { path: '/dashboardmetric', name: 'dashboardmetric', component: Dashboardmetric },
    { path: '/staff', name: 'staff', component: Staff },
    { path: '/area', name: 'area', component: Area },
    { path: '/shift', name: 'shift', component: Shift },
    { path: '/notice', name: 'notice', component: Notice },
    { path: '/auditlog', name: 'auditlog', component: Auditlog },
    { path: '/report', name: 'report', component: Report },
    { path: '/dict', name: 'dict', component: Dict },
    { path: '/setting', name: 'setting', component: Setting },
  ],
})

export default router

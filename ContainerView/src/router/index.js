// vue路由
// 单页面应用核心功能

import HomePage from '@/views/HomePage.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
        path: '/',
        name: 'home',
        component: HomePage,
        },
        {
            path: '/login',
            name: 'login',
            component: ()=>import('@/views/Login.vue'),
        },
        {
            path: '/add',
            name: 'add',
            component: ()=>import('@/views/Add.vue'),
        },
        {
            path: '/control',
            name: 'control',
            component: ()=>import('@/views/Control.vue'),
        },
        {
            path: '/container',
            name: 'container',
            component: ()=>import('@/views/Container.vue'),
        },
    ],
});

export default router;

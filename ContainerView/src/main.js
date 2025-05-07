// 入口脚本

// vue基本
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router';

// 导入库
// 用户界面样式 BootStrap
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap';
import 'axios'; // 异步请求

// 创建web应用 挂载html
const app = createApp(App);
app.use(createPinia());
app.use(router);
app.mount('#app');

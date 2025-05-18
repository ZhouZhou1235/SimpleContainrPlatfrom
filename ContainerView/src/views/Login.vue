<!-- 登录 -->

<script setup>
    import { postRequest } from '@/api/HttpRequest';
    import { urls } from '@/vars/urls';
    import router from '@/router';
    import { GStoreArea } from '@/stores/GStoreArea';
</script>

<template>
  <div class="login-page">
    <div class="login-container">
      <div class="login-header">
        <span class="icon-container"></span>
        <h1>集装箱平台</h1>
        <p>请登录或注册以继续使用</p>
      </div>

      <div class="form-selector">
        <button @click="activeForm = 'userLogin'" :class="{ active: activeForm === 'userLogin' }">用户登录</button>
        <button @click="activeForm = 'userRegister'" :class="{ active: activeForm === 'userRegister' }">用户注册</button>
        <button @click="activeForm = 'adminLogin'" :class="{ active: activeForm === 'adminLogin' }">管理员登录</button>
      </div>

      <div class="form-content">
        <!-- 用户登录表单 -->
        <form v-if="activeForm === 'userLogin'" @submit.prevent="login" class="login-form">
          <div class="form-group">
            <label for="login-username"><i class="fas fa-user"></i> 账号</label>
            <input id="login-username" type="text" v-model="loginForm.username" placeholder="请输入用户账号" required>
          </div>
          <div class="form-group">
            <label for="login-password"><i class="fas fa-lock"></i> 密码</label>
            <input id="login-password" type="password" v-model="loginForm.password" placeholder="请输入密码" required>
          </div>
          <button type="submit" class="btn-submit">登录</button>
        </form>

        <!-- 用户注册表单 -->
        <form v-if="activeForm === 'userRegister'" @submit.prevent="register" class="login-form">
          <div class="form-group">
            <label for="register-username"><i class="fas fa-user-plus"></i> 账号</label>
            <input id="register-username" type="text" v-model="registerForm.username" placeholder="请输入注册账号" required>
          </div>
          <div class="form-group">
            <label for="register-password"><i class="fas fa-lock"></i> 密码</label>
            <input id="register-password" type="password" v-model="registerForm.password" placeholder="请输入密码" required>
          </div>
          <div class="form-group">
            <label for="register-name"><i class="fas fa-id-card"></i> 名称</label>
            <input id="register-name" type="text" v-model="registerForm.name" placeholder="请输入您的名称" required>
          </div>
          <div class="form-group">
            <label for="register-info"><i class="fas fa-info-circle"></i> 介绍</label>
            <input id="register-info" type="text" v-model="registerForm.info" placeholder="简单介绍一下自己">
          </div>
          <div class="form-group">
            <label for="register-type"><i class="fas fa-tag"></i> 类型</label>
            <input id="register-type" type="text" v-model="registerForm.type" placeholder="用户类型 (例如: 货主, 承运商)">
          </div>
          <button type="submit" class="btn-submit">注册</button>
        </form>

        <!-- 管理员登录表单 -->
        <form v-if="activeForm === 'adminLogin'" @submit.prevent="adminLogin" class="login-form">
          <div class="form-group">
            <label for="admin-username"><i class="fas fa-user-shield"></i> 管理员账号</label>
            <input id="admin-username" type="text" v-model="adminLoginForm.admin" placeholder="请输入管理员账号" required>
          </div>
          <div class="form-group">
            <label for="admin-password"><i class="fas fa-key"></i> 密码</label>
            <input id="admin-password" type="password" v-model="adminLoginForm.password" placeholder="请输入管理员密码" required>
          </div>
          <button type="submit" class="btn-submit">管理员登录</button>
        </form>
      </div>
      
      <div class="footer-text">
        集装箱平台 - 数据库航运课程设计
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        data(){
            return{
                activeForm: 'userLogin', // 'userLogin', 'userRegister', 'adminLogin',
                loginForm: {
                    username: '',
                    password: '',
                },
                registerForm: {
                    username: '',
                    password: '',
                    name: '',
                    info: '',
                    type: '',
                },
                adminLoginForm: {
                    admin: '',
                    password: '',
                },
            }
        },
        methods: {
            login(){
                postRequest(urls.doLogin,this.loginForm).then(res=>{
                    if(!res){return;}
                    let GStore = GStoreArea();
                    // GStore.setLogin(true); // 假设 GStore.getAndSetUser 会处理登录状态
                    // GStore.setAdmin(false);
                    GStore.getAndSetUser(this.loginForm.username);
                    router.push(urls.homePage || '/'); // 使用在 urls.js 中定义的首页路由
                });
            },
            register(){
                postRequest(urls.doRegister,this.registerForm).then(res=>{
                    if(!res){return;}
                    alert("注册成功，请登录！");
                    this.activeForm = 'userLogin'; // 注册成功后跳转到登录表单
                    // 不需要立即登录或跳转，让用户手动登录
                });
            },
            adminLogin(){
                postRequest(urls.adminDologin,this.adminLoginForm).then(res=>{
                    if(!res){return;}
                    let GStore = GStoreArea();
                    // GStore.setLogin(true);
                    // GStore.setAdmin(true);
                    GStore.getAndSetAdmin(); // 假设此方法会设置管理员状态和名称
                    router.push(urls.controlPage || '/control'); // 使用在 urls.js 中定义的控制台路由
                });
            },
        },
    }

</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); /* 更现代的渐变背景 */
  padding: 20px;
  font-family: 'Roboto', 'Helvetica Neue', Helvetica, Arial, sans-serif; /* 更改字体 */
}

.login-container {
  background-color: rgba(255, 255, 255, 0.95); /* 轻微透明背景 */
  padding: 35px 45px; /* 增加内边距 */
  border-radius: 12px; /* 更大的圆角 */
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15); /* 更柔和的阴影 */
  width: 100%;
  max-width: 480px; /* 略微增加最大宽度 */
  text-align: center;
  backdrop-filter: blur(5px); /* 毛玻璃效果 (如果背景部分透明) */
}

.login-header {
  margin-bottom: 30px; /* 增加间距 */
}

.login-header .icon-container {
  font-size: 48px; /* 增大图标 */
  color: #5e72e4; /* 主题色调整 - 鲜艳蓝紫色 */
  margin-bottom: 15px;
  display: inline-block;
  transition: transform 0.3s ease;
}

.login-header .icon-container:hover {
  transform: scale(1.1); /* 图标悬停放大 */
}

.login-header h1 {
  font-size: 28px; /* 增大标题字号 */
  color: #333;
  margin-bottom: 8px;
  font-weight: 700; /* 加粗 */
}

.login-header p {
  font-size: 16px;
  color: #555; /* 调整颜色 */
}

.form-selector {
  display: flex;
  justify-content: center;
  margin-bottom: 30px;
  border-bottom: 2px solid #e0e0e0; /* 边框线调整 */
}

.form-selector button {
  background: none;
  border: none;
  padding: 12px 20px; /* 调整按钮内边距 */
  cursor: pointer;
  font-size: 16px; /* 调整字体大小 */
  color: #666;
  position: relative;
  transition: color 0.3s ease, font-weight 0.3s ease;
  outline: none;
  font-weight: 500;
}

.form-selector button.active {
  color: #5e72e4; /* 主题色 */
  font-weight: 700;
}

.form-selector button.active::after {
  content: '';
  position: absolute;
  bottom: -2px; /* 调整位置以匹配边框线 */
  left: 0;
  width: 100%;
  height: 3px;
  background-color: #5e72e4; /* 主题色 */
  border-radius: 2px;
}

.login-form .form-group {
  margin-bottom: 20px; /* 调整间距 */
  text-align: left;
}

.login-form label {
  display: block;
  margin-bottom: 8px; /* 调整间距 */
  font-weight: 600; /* 加粗标签 */
  color: #495057; /* 深灰色 */
  font-size: 14px;
}

.login-form label i {
  margin-right: 8px; /* 调整图标间距 */
  color: #5e72e4; /* 主题色 */
  width: 18px; /* 固定图标宽度 */
  text-align: center;
}

.login-form input[type="text"],
.login-form input[type="password"] {
  width: 100%;
  padding: 12px 15px; /* 调整输入框内边距 */
  border: 1px solid #ced4da;
  border-radius: 6px; /* 更大的圆角 */
  box-sizing: border-box;
  font-size: 15px;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
  background-color: #f8f9fa; /* 输入框背景色 */
}

.login-form input[type="text"]::placeholder,
.login-form input[type="password"]::placeholder {
  color: #adb5bd;
}

.login-form input[type="text"]:focus,
.login-form input[type="password"]:focus {
  border-color: #5e72e4;
  outline: none;
  box-shadow: 0 0 0 3px rgba(94, 114, 228, 0.25); /* 调整焦点阴影 */
  background-color: #fff;
}

.btn-submit {
  width: 100%;
  padding: 12px; /* 调整按钮内边距 */
  background-color: #5e72e4; /* 主题色 */
  color: white;
  border: none;
  border-radius: 6px; /* 更大的圆角 */
  cursor: pointer;
  font-size: 17px; /* 调整字体大小 */
  font-weight: 600;
  transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.2s ease;
  margin-top: 15px;
  letter-spacing: 0.5px; /* 增加字间距 */
}

.btn-submit:hover {
  background-color: #4a5cc0; /* 悬停颜色加深 */
  box-shadow: 0 4px 15px rgba(94, 114, 228, 0.35);
}

.btn-submit:active {
  transform: translateY(2px);
  box-shadow: 0 2px 8px rgba(94, 114, 228, 0.3);
}

.footer-text {
  margin-top: 30px; /* 调整间距 */
  font-size: 13px;
  color: #888;
}

/* 添加一些动画效果 */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.login-container > * {
  animation: fadeIn 0.5s ease-out forwards;
}

.login-header h1, .login-header p, .form-selector, .form-content, .footer-text {
  animation-delay: 0.1s;
}

.form-selector button {
   animation-delay: 0.2s;
}

.login-form .form-group {
  animation: fadeIn 0.4s ease-out forwards;
  opacity: 0; /* Start hidden for staggered animation */
}

/* Stagger animation for form groups */
.login-form .form-group:nth-child(1) { animation-delay: 0.3s; }
.login-form .form-group:nth-child(2) { animation-delay: 0.4s; }
.login-form .form-group:nth-child(3) { animation-delay: 0.5s; }
.login-form .form-group:nth-child(4) { animation-delay: 0.6s; }
.login-form .form-group:nth-child(5) { animation-delay: 0.7s; }
.btn-submit { animation-delay: 0.8s; }

</style>



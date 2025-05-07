<!-- 登录 -->

<script setup>
    import { postRequest } from '@/api/HttpRequest';
    import { urls } from '@/vars/urls';
    import router from '@/router';
    import { GStoreArea } from '@/stores/GStoreArea';
</script>

<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-4">
                <h2>用户登录</h2>
                <div class="form-label">账号</div>
                <input type="text" v-model="loginForm.username" class="form-control">
                <div class="form-label">密码</div>
                <input type="password" v-model="loginForm.password" class="form-control">
                <div class="d-grid">
                    <button v-on:click="login()" class="btn">登录</button>
                </div>
            </div>
            <div class="col-sm-4">
                <h2>用户注册</h2>
                <div class="form-label">账号</div>
                <input type="text" v-model="registerForm.username" class="form-control">
                <div class="form-label">密码</div>
                <input type="password" v-model="registerForm.password" class="form-control">
                <div class="form-label">名称</div>
                <input type="text" v-model="registerForm.name" class="form-control">
                <div class="form-label">介绍</div>
                <input type="text" v-model="registerForm.info" class="form-control">
                <div class="form-label">类型</div>
                <input type="text" v-model="registerForm.type" class="form-control">
                <div class="d-grid">
                    <button v-on:click="register()" class="btn">注册</button>
                </div>
            </div>
            <div class="col-sm-4">
                <h2>管理员登录</h2>
                <div class="form-label">管理员账号</div>
                <input type="text" v-model="adminLoginForm.admin" class="form-control">
                <div class="form-label">密码</div>
                <input type="password" v-model="adminLoginForm.password" class="form-control">
                <div class="d-grid">
                    <button v-on:click="adminLogin()" class="btn">管理员登录</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data(){return{
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
        }},
        methods: {
            login(){
                postRequest(urls.doLogin,this.loginForm).then(res=>{
                    if(!res){return;}
                    let GStore = GStoreArea();
                    GStore.getAndSetUser(this.loginForm.username);
                    router.push('/');
                });
            },
            register(){
                postRequest(urls.doRegister,this.registerForm).then(res=>{
                    if(!res){return;}
                    let GStore = GStoreArea();
                    GStore.getAndSetUser(this.registerForm.username);
                    router.push('/');
                });
            },
            adminLogin(){
                postRequest(urls.adminDologin,this.adminLoginForm).then(res=>{
                    if(!res){return;}
                    let GStore = GStoreArea();
                    GStore.getAndSetAdmin();
                    router.push('/');
                });
            },
        },
    }
</script>

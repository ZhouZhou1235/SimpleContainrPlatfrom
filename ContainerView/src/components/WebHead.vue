<script setup>
    import { getRequest, postRequest } from '@/api/HttpRequest';
    import { urls } from '@/vars/urls';
    import { GStoreArea } from '@/stores/GStoreArea';
    import router from '@/router';
    const GStore = GStoreArea();
</script>

<template>
    <div class="container text-center">
        <h1>集装箱平台</h1>
        <RouterLink to="/" class="p-2"><button class="btn">主页</button></RouterLink>
        <RouterLink to="login" v-if="!GStore.admin.isLog && !GStore.user.isLog" class="p-2"><button class="btn">登录</button></RouterLink>
        <RouterLink to="control" v-if="GStore.admin.isLog" class="p-2"><button class="btn">管理面板</button></RouterLink>
        <RouterLink to="add" v-if="GStore.user.isLog" class="p-2"><button class="btn">添加</button></RouterLink>
        <button v-on:click="logout()" v-if="GStore.admin.isLog || GStore.user.isLog" class="p-2 btn">注销</button>
    </div>
</template>

<script>
    export default {
        data(){return{}},
        methods: {
            logout(){
                postRequest(urls.logout);
                router.push('/');
                location.reload();
            },
        },
    }
</script>

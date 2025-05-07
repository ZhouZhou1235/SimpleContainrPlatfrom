<script setup>
import { getRequest, postRequest } from '@/api/HttpRequest';
import router from '@/router';
import { urls } from '@/vars/urls';


</script>

<template>
    <div class="container">
        <h1>管理面板</h1>
        <div class="row">
            <div class="col-sm-4">
                <h2>操作区域</h2>
                <div class="container">
                    <h3>集装箱</h3>
                    <span v-if="containerForm.containerid">正在编辑 {{ containerForm.containerid }}</span>
                    <div class="form-label">名称</div>
                    <input type="text" v-model="containerForm.title" class="form-control">
                    <div class="form-label">描述</div>
                    <textarea v-model="containerForm.info" class="form-control"></textarea>
                    <div class="d-grid">
                        <button v-on:click="updateContainer()" class="btn">修改</button>
                    </div>
                    <div class="d-grid">
                        <button v-on:click="deleteContainer()" class="btn">删除</button>
                    </div>
                </div>
                <div class="container">
                    <h3>公司</h3>
                    <span v-if="companyForm.companyid">正在编辑 {{ companyForm.companyid }}</span>
                    <div class="form-label">公司全称</div>
                    <input type="text" v-model="companyForm.name" class="form-control">
                    <div class="form-label">描述</div>
                    <textarea v-model="companyForm.info" class="form-control"></textarea>
                    <div class="d-grid">
                        <button v-on:click="updateCompany()" class="btn">修改</button>
                    </div>
                    <div class="d-grid">
                        <button v-on:click="deleteCompany()" class="btn">删除</button>
                    </div>
                </div>
                <div class="container">
                    <h3>用户</h3>
                    <span v-if="userForm.username">正在编辑 {{ userForm.username }}</span>
                    <div class="form-label">名称</div>
                    <input type="text" v-model="userForm.name" class="form-control">
                    <div class="form-label">介绍</div>
                    <input type="text" v-model="userForm.info" class="form-control">
                    <div class="form-label">类型</div>
                    <input type="text" v-model="userForm.type" class="form-control">
                    <div class="d-grid">
                        <button v-on:click="updateUser()" class="btn">修改</button>
                    </div>
                    <div class="d-grid">
                        <button v-on:click="deleteUser()" class="btn">删除</button>
                    </div>
                </div>
            </div>
            <div class="col-sm-8">
                <div>
                    <h2>集装箱</h2>
                    <div v-for="item in containerArray" class="list-group">
                        <div class="list-group-item">
                            <button
                                v-on:click="setContainerForm({
                                    'containerid':item.containerid,
                                    'title':item.title,
                                    'info': item.info,
                                })"
                                class="btn"
                            >
                                编辑
                            </button>
                            <RouterLink v-bind:to="'/container?containerid='+item.containerid">
                                {{ item.title }}
                            </RouterLink>
                            描述 {{ item.info }}
                            <span v-if="!item.exittime">{{ toNormalDate(item.entertime) }}入库</span>
                            <span v-else>{{ toNormalDate(item.exittime) }}离库</span>
                        </div>
                    </div>
                </div>
                <div>
                    <h2>公司</h2>
                    <div v-for="item in companyArray" class="list-group">
                        <div class="list-group-item">
                            <button
                                v-on:click="setCompanyForm({
                                    'companyid':item.companyid,
                                    'name':item.name,
                                    'info':item.info,
                                })"
                                class="btn"
                            >
                                编辑
                            </button>
                            ID {{ item.companyid }}
                            公司 {{ item.name }}
                            介绍 {{ item.info }}
                        </div>
                    </div>
                </div>
                <div>
                    <h2>用户</h2>
                    <div v-for="item in userArray" class="list-group">
                        <div class="list-group-item">
                            <button
                                v-on:click="setUserForm({
                                    'username':item.username,
                                    'name':item.name,
                                    'info':item.info,
                                    'type':item.type,
                                })"
                                class="btn"
                            >
                                编辑
                            </button>
                            用户ID {{ item.username }}
                            用户 {{ item.name }}
                            类型 {{ item.type }}
                            介绍 {{ item.info }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data(){return{
            containerArray: [],
            companyArray: [],
            userArray: [],
            containerForm: {
                containerid: '',
                title: '',
                info: '',
            },
            companyForm: {
                companyid: '',
                name: '',
                info: '',
            },
            userForm: {
                username: '',
                name: '',
                info: '',
                type: '',
            },
        }},
        methods: {
            getContainers(){
                getRequest(urls.getContainers).then(res=>{
                    if(res!='no data'){
                        this.containerArray = res.data;
                    }
                });
            },
            getCompanys(){
                getRequest(urls.getCompanys).then(res=>{
                    if(res!='no data'){
                        this.companyArray = res.data;
                    }
                });
            },
            getUsers(){
                getRequest(urls.getUsers).then(res=>{
                    if(res!='no data'){
                        this.userArray = res.data;
                    }
                });
            },
            setContainerForm(obj){
                this.containerForm.containerid = obj.containerid;
                this.containerForm.title = obj.title;
                this.containerForm.info = obj.info;

            },
            setCompanyForm(obj){
                this.companyForm.companyid = obj.companyid;
                this.companyForm.name = obj.name;
                this.companyForm.info = obj.info;
            },
            setUserForm(obj){
                this.userForm.username = obj.username;
                this.userForm.name = obj.name;
                this.userForm.info = obj.info;
                this.userForm.type = obj.type;
            },
            updateContainer(){
                postRequest(urls.updateContainer,this.containerForm).then(res=>{
                    if(res==1){
                        router.push('/control');
                    }
                });
            },
            updateCompany(){
                postRequest(urls.updateCompany,this.companyForm).then(res=>{
                    if(res==1){
                        router.push('/control');
                    }
                });
            },
            updateUser(){
                postRequest(urls.updateUser,this.userForm).then(res=>{
                    if(res==1){
                        router.push('/control');
                    }
                });
            },
            deleteContainer(){
                postRequest(urls.deleteContainer,this.containerForm).then(res=>{
                    if(res==1){
                        router.push('/control');
                    }
                });
            },
            deleteCompany(){
                postRequest(urls.deleteCompany,this.companyForm).then(res=>{
                    if(res==1){
                        router.push('/control');
                    }
                });
            },
            deleteUser(){
                postRequest(urls.deleteUser,this.userForm).then(res=>{
                    if(res==1){
                        router.push('/control');
                    }
                });
            },
            toNormalDate(time){
                let date = new Date(time);
                return date.toLocaleString();
            },
        },
        mounted(){
            this.getContainers();
            this.getCompanys();
            this.getUsers();
        },
    }
</script>

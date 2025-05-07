<!-- 内容添加 -->

<script setup>
import { postRequest } from '@/api/HttpRequest';
import router from '@/router';
import { urls } from '@/vars/urls';

</script>

<template>
    <div class="container">
        <div class="p-3">
            <h2>添加集装箱</h2>
            <div class="row">
                <div class="col-sm-6">
                    <h3>集装箱</h3>
                    <div class="form-label">公司ID</div>
                    <input type="text" v-model="containerForm.companyid" class="form-control">
                    <div class="form-label">名称</div>
                    <input type="text" v-model="containerForm.title" class="form-control">
                    <div class="form-label">描述</div>
                    <textarea v-model="containerForm.info" class="form-control"></textarea>
                </div>
                <div class="col-sm-6">
                    <div>
                        <h3>货物</h3>
                        <p>
                            输入格式<br>
                            a名称 a数量<br>
                            b名称 b数量<br>
                            ...
                        </p>
                        <textarea v-model="containerForm.cargoText" class="form-control" rows="4"></textarea>
                    </div>
                    <div class="d-grid">
                        <button v-on:click="addContainer()" class="btn">添加</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="p-3">
            <h2>添加公司</h2>
            <div class="form-label">公司全称</div>
            <input type="text" v-model="companyForm.name" class="form-control">
            <div class="form-label">描述</div>
            <textarea v-model="companyForm.info" class="form-control" rows="4"></textarea>
            <div class="d-grid">
                <button v-on:click="addCompany()" class="btn">添加</button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data(){return{
            containerForm: {
                companyid: '',
                title: '',
                info: '',
                cargoText: '',
            },
            companyForm: {
                name: '',
                info: '',
            },
        }},
        methods: {
            addContainer(){
                postRequest(urls.addContainer,this.containerForm).then(res=>{
                    if(res==1){router.push('/');}
                });
            },
            addCompany(){
                postRequest(urls.addCompany,this.companyForm).then(res=>{
                    if(res==1){router.push('/')}
                });
            }
        },
    }
</script>

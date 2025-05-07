<!-- 首页 -->

<script setup>
    import { getRequest, postRequest } from '@/api/HttpRequest';
import { GStoreArea } from '@/stores/GStoreArea';
    import { urls } from '@/vars/urls';
    const GStore = GStoreArea();
</script>

<template>
    <div class="container">
        <div class="p-3">
            <h2>集装箱仓库</h2>
            <div v-for="item in containerArray" class="row p-2">
                <div class="col-sm-3">
                    <div class="card">
                        <div class="card-body">
                            <h3 class="card-title">
                                <RouterLink v-bind:to="'/container?containerid='+item.containerid">
                                    {{ item.title }}
                                </RouterLink>
                            </h3>
                            <p class="card-text">{{ item.info }}</p>
                            <span v-if="!item.exittime">{{ toNormalDate(item.entertime) }}入库</span>
                            <span v-else>{{ toNormalDate(item.exittime) }}离库</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="GStore.user.isLog" class="p-3">
            <h2>用户集装箱</h2>
            <div v-for="item in myContainerArray" class="row p-2">
                <div class="col-sm-3">
                    <div class="card">
                        <div class="card-body">
                            <h3 class="card-title">
                                <RouterLink v-bind:to="'/container?containerid='+item.containerid">
                                    {{ item.title }}
                                </RouterLink>
                            </h3>
                            <p class="card-text">{{ item.info }}</p>
                            <span v-if="!item.exittime"><button v-on:click="containerExit(item.containerid)" class="btn">离库</button></span>
                            <span v-else>{{ toNormalDate(item.exittime) }}离库</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="p-3">
            <h2>公司列表</h2>
            <div v-for="item in companyArray" class="list-group p-2">
                <div class="list-group-item">
                    <div class="row">
                    <div class="col-2">
                        {{ item.companyid }}
                    </div>
                    <div class="col-2">
                        {{ item.name }}
                    </div>
                    <div class="col-8">
                        {{ item.info }}
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
            myContainerArray: [],
            companyArray: [],
        }},
        methods: {
            getContainers(){
                getRequest(urls.getContainers).then(res=>{
                    if(res!='no data'){
                        this.containerArray = res.data;
                    }
                });
            },
            getMyContainers(){
                getRequest(urls.getContainerByUsername).then(res=>{
                    if(res!='no data'){
                        this.myContainerArray = res.data;
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
            containerExit(containerid){
                postRequest(urls.containerExit,{'containerid':containerid}).then(res=>{
                    if(res==1){
                        this.getMyContainers();
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
            this.getMyContainers();
            this.getCompanys();
        },
    }
</script>

<script setup>
    import { getRequest } from '@/api/HttpRequest';
    import { urls } from '@/vars/urls';
</script>

<template>
    <div v-if="containerData!=null" class="container">
        <div class="row">
            <div class="col-sm-4">
                <h1>{{ containerData.container.title }}</h1>
                <p style="white-space: pre-line;">
                    {{ containerData.container.info }}
                </p>
                <p>
                    入库 {{ toNormalDate(containerData.containerRegister.entertime) }}
                    <br>
                    <span v-if="containerData.containerRegister.exittime">出库 {{ toNormalDate(containerData.containerRegister.exittime) }}</span>
                </p>
                <div>
                    <h3>用户</h3>
                    <div>
                        {{ containerData.user.type }}
                        |
                        {{ containerData.user.name }}
                        |
                        {{ containerData.user.info }}
                    </div>
                </div>
                <div v-if="containerData.company!=null">
                    <h3>公司</h3>
                    <div>
                        {{ containerData.company.companyid }}
                        |
                        {{ containerData.company.name }}
                        |
                        {{ containerData.company.info }}
                    </div>
                </div>
            </div>
            <div class="col-sm-8">
                <h2>货物</h2>
                <div v-for="item in containerData.cargo" class="list-group">
                    <div class="list-group-item">
                        货物名称 {{ item.title }}
                        |
                        数量 {{ item.num }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data(){return{
            containerid: null,
            containerData: null,
        }},
        methods: {
            getToShowContainer(){
                let id = this.$route.query.containerid;
                this.containerid = id;
                getRequest(urls.getContainerFull+id).then(res=>{
                    if(res!='no data'){
                        this.containerData = res;
                    }
                });
            },
            toNormalDate(time){
                let date = new Date(time);
                return date.toLocaleString();
            },
        },
        mounted(){
            this.getToShowContainer();
        },
    }
</script>

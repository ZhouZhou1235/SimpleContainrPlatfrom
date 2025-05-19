<!-- 首页 -->

<script setup>
    import { getRequest, postRequest } from '@/api/HttpRequest';
import { GStoreArea } from '@/stores/GStoreArea';
    import { urls } from '@/vars/urls';
    const GStore = GStoreArea();
</script>

<template>
  <WebHead />
  <div class="home-page-bg">
    <div class="home-page-flex">
      <!-- 集装箱仓库模块 -->
      <div class="content-container home-module">
        <h2 class="section-title">集装箱仓库</h2>
        <div v-for="item in containerArray" :key="item.containerid" class="p-2">
          <div class="card">
            <div class="card-body">
              <h3 class="card-title">
                <RouterLink :to="'/container?containerid='+item.containerid">
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
      <!-- 用户集装箱模块 -->
      <div v-if="GStore.user.isLog" class="content-container home-module">
        <h2 class="section-title">用户集装箱</h2>
        <div v-for="item in myContainerArray" :key="item.containerid" class="p-2">
          <div class="card">
            <div class="card-body">
              <h3 class="card-title">
                <RouterLink :to="'/container?containerid='+item.containerid">
                  {{ item.title }}
                </RouterLink>
              </h3>
              <p class="card-text">{{ item.info }}</p>
              <span v-if="item.exittime">
                {{ toNormalDate(item.exittime) }}离库
              </span>
            </div>
          </div>
        </div>
      </div>
      <!-- 公司列表模块 -->
      <div class="content-container home-module">
        <h2 class="section-title">公司列表</h2>
        <div v-for="item in companyArray" :key="item.companyid" class="list-group p-2">
          <div class="list-group-item">
            <div class="row">
              <div class="col-2">{{ item.companyid }}</div>
              <div class="col-2">{{ item.name }}</div>
              <div class="col-8">{{ item.info }}</div>
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

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

.home-page-bg {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.home-page-flex {
  display: flex;
  flex-direction: row;
  justify-content: center;
  gap: 32px;
  width: 100%;
  max-width: 1400px;
}

.content-container.home-module {
  background-color: rgba(255, 255, 255, 0.95);
  padding: 30px 24px;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
  min-width: 320px;
  max-width: 400px;
  flex: 1 1 0;
  margin-bottom: 20px;
  backdrop-filter: blur(5px);
  text-align: left;
  display: flex;
  flex-direction: column;
}

.section-title {
  font-size: 22px;
  color: #333;
  margin-bottom: 18px;
  font-weight: 700;
  border-bottom: 2px solid #5e72e4;
  padding-bottom: 8px;
  display: inline-block;
}

.card {
  margin-bottom: 16px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(94, 114, 228, 0.08);
  border: none;
}

.card-title a {
  color: #2962ff;
  text-decoration: underline;
  font-weight: 600;
  font-size: 20px;
}

.card-title a:hover {
  color: #5e72e4;
}

.card-text {
  color: #495057;
  font-size: 15px;
  margin-bottom: 8px;
}

.btn {
  background-color: #5e72e4;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 6px 16px;
  font-size: 15px;
  cursor: pointer;
  transition: background 0.2s;
}

.btn:hover {
  background-color: #4a5cc0;
}

@media (max-width: 1100px) {
  .home-page-flex {
    flex-direction: column;
    align-items: center;
    gap: 24px;
  }
  .content-container.home-module {
    max-width: 95vw;
    min-width: 0;
  }
}
</style>

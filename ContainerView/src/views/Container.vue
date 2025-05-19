<script setup>
    import { getRequest } from '@/api/HttpRequest';
    import { urls } from '@/vars/urls';
    import WebFooter from '@/components/WebFooter.vue'; // 引入 WebFooter 组件
</script>

<template>
  <WebHead />
  <div class="container-page-wrapper">
    <div class="top-bar">
      <button class="back-btn" @click="$router.go(-1)"><i class="fas fa-arrow-left"></i> 返回上一页</button>
    </div>
    <div v-if="containerData!=null" class="content-container">
        <div class="row">
            <div class="col-sm-4">
                <div class="page-header">
                  <h1>{{ containerData.container.title }}</h1>
                </div>
                <div class="info-section">
                  <h3><i class="fas fa-info-circle"></i> 基本信息</h3>
                  <p style="white-space: pre-line;">
                      {{ containerData.container.info }}
                  </p>
                  <p>位置 {{ containerData.container.position }}</p>
                </div>
                <div class="info-section date-info">
                  <h3><i class="fas fa-calendar-alt"></i> 日期信息</h3>
                  <p>
                      <span><strong>入库时间:</strong> {{ toNormalDate(containerData.containerRegister.entertime) }}</span>
                      <span v-if="containerData.containerRegister.exittime"><strong>出库时间:</strong> {{ toNormalDate(containerData.containerRegister.exittime) }}</span>
                  </p>
                </div>
                <div class="info-section">
                    <h3><i class="fas fa-user"></i> 用户信息</h3>
                    <div>
                        <strong>类型:</strong> {{ containerData.user.type }} <br>
                        <strong>名称:</strong> {{ containerData.user.name }} <br>
                        <strong>介绍:</strong> {{ containerData.user.info }}
                    </div>
                </div>
                <div v-if="containerData.company!=null" class="info-section">
                    <h3><i class="fas fa-building"></i> 公司信息</h3>
                    <div>
                        <strong>ID:</strong> {{ containerData.company.companyid }} <br>
                        <strong>名称:</strong> {{ containerData.company.name }} <br>
                        <strong>介绍:</strong> {{ containerData.company.info }}
                    </div>
                </div>
            </div>
            <div class="col-sm-8 cargo-section">
                <h2><i class="fas fa-box-open"></i> 货物列表</h2>
                <div v-if="containerData.cargo && containerData.cargo.length > 0" class="list-group">
                    <div v-for="item in containerData.cargo" :key="item.cargoid" class="list-group-item">
                        <strong>货物名称:</strong> {{ item.title }}
                        |
                        <strong>数量:</strong> {{ item.num }}
                    </div>
                </div>
                <div v-else class="list-group-item">
                    暂无货物信息。
                </div>
            </div>
        </div>
      </div>
      <div v-else class="loading-text">
        正在加载集装箱数据...
      </div>
    </div>
  <WebFooter />
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

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

.container-page-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px;
  padding-bottom: 70px; /* 为固定页脚预留空间 */
  font-family: 'Roboto', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  box-sizing: border-box;
}

.content-container {
  background-color: rgba(255, 255, 255, 0.95);
  padding: 30px 40px;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
  width: 100%;
  max-width: 1000px; /* Adjusted for content layout */
  margin-top: 20px;
  margin-bottom: 20px;
  backdrop-filter: blur(5px);
  text-align: left;
}

.page-header h1 {
  font-size: 28px;
  color: #333;
  margin-bottom: 15px;
  font-weight: 700;
  color: #5e72e4; /* Theme color for title */
}

.info-section {
  margin-bottom: 25px;
}

.info-section h3 {
  font-size: 20px;
  color: #495057;
  margin-bottom: 10px;
  font-weight: 600;
  border-bottom: 1px solid #e0e0e0;
  padding-bottom: 5px;
}

.info-section p,
.info-section div {
  font-size: 15px;
  color: #555;
  line-height: 1.7;
  margin-bottom: 8px;
}

.info-section p strong {
  color: #333;
  font-weight: 600;
}

.info-section .date-info span {
  display: block; /* Dates on new lines */
  margin-bottom: 5px;
}

.cargo-section h2 {
  font-size: 24px;
  color: #333;
  margin-bottom: 20px;
  font-weight: 700;
  border-bottom: 2px solid #5e72e4;
  padding-bottom: 10px;
  display: inline-block;
}

.list-group-item {
  background-color: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  margin-bottom: 10px;
  padding: 15px;
  transition: box-shadow 0.3s ease;
  font-size: 15px;
  color: #495057;
}

.list-group-item:hover {
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.list-group-item strong {
  color: #5e72e4; /* Theme color for emphasis */
}

/* Responsive adjustments */
.row {
  margin-left: -15px;
  margin-right: -15px;
}
.col-sm-4, .col-sm-8 {
  padding-left: 15px;
  padding-right: 15px;
}

.loading-text {
  text-align: center;
  font-size: 18px;
  color: #fff;
  padding: 50px;
}

.top-bar {
  width: 100%;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  margin-bottom: 10px;
}
.back-btn {
  background: #5e72e4;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 8px 18px;
  font-size: 15px;
  cursor: pointer;
  transition: background 0.2s;
  margin-top: 10px;
  margin-right: 10px;
}
.back-btn:hover {
  background: #324cdd;
}
</style>

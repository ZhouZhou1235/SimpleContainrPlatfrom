<script setup>
import { getRequest, postRequest } from '@/api/HttpRequest';
import router from '@/router';
import { urls } from '@/vars/urls';
import WebFooter from '@/components/WebFooter.vue'; // 引入 WebFooter 组件

</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

.control-page-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
  background-color: #f4f7f9; /* 更柔和的背景色 */
  padding: 20px;
  padding-bottom: 70px; /* 为固定页脚预留空间 */
  font-family: 'Roboto', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  box-sizing: border-box;
}

.content-container {
  background-color: #ffffff; /* 纯白背景 */
  padding: 30px 40px;
  border-radius: 12px;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1); /* 更柔和的阴影 */
  width: 100%;
  max-width: 1400px; /* Wider for control panel layout */
  margin-top: 20px;
  margin-bottom: 20px;
  /* backdrop-filter: blur(5px); /* 移除毛玻璃效果，如果背景是纯色则不需要 */
  text-align: left;
}

.page-title {
  font-size: 28px;
  color: #333;
  margin-bottom: 30px;
  font-weight: 700;
  text-align: center;
  width: 100%;
}

.section-title {
  font-size: 22px;
  color: #333;
  margin-bottom: 20px;
  font-weight: 600;
  border-bottom: 2px solid #5e72e4;
  padding-bottom: 8px;
  display: inline-block;
}

.form-section {
  background-color: var(--surface); /* 使用 global.css 变量 */
  padding: var(--spacing-lg); /* 使用 global.css 变量 */
  border-radius: 8px;
  margin-bottom: 30px;
  box-shadow: var(--shadow-1); /* 使用 global.css 变量 */
}

.form-section h3 {
  font-size: 18px;
  color: #495057;
  margin-bottom: 15px;
  font-weight: 600;
}

.form-label {
  display: block;
  margin-bottom: 6px;
  font-weight: 600;
  color: #495057;
  font-size: 14px;
}

.form-control {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #ced4da;
  border-radius: 6px;
  box-sizing: border-box;
  font-size: 14px;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
  background-color: #fff; /* Slightly different from Add.vue for contrast */
  margin-bottom: 12px;
}

.form-control:focus {
  border-color: #5e72e4;
  outline: none;
  box-shadow: 0 0 0 3px rgba(94, 114, 228, 0.25);
}

textarea.form-control {
  min-height: 80px;
  resize: vertical;
}

.editing-indicator {
  font-size: 13px;
  color: #5e72e4;
  margin-bottom: 10px;
  font-style: italic;
}

.btn-action {
  width: 100%;
  padding: 10px;
  background-color: #5e72e4;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 15px;
  font-weight: 500;
  transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.2s ease;
  margin-top: 8px;
  margin-bottom: 8px; /* Space between buttons */
  letter-spacing: 0.3px;
}

.btn-action:hover {
  background-color: #4a5cc0;
  box-shadow: 0 2px 10px rgba(94, 114, 228, 0.3);
}

.btn-action:active {
  transform: translateY(1px);
  box-shadow: 0 1px 5px rgba(94, 114, 228, 0.25);
}

.btn-delete {
  background-color: #e74c3c; /* Red for delete */
}

.btn-delete:hover {
  background-color: #c0392b;
  box-shadow: 0 2px 10px rgba(231, 76, 60, 0.3);
}

.lists-container-horizontal {
  display: flex;
  flex-direction: row; /* 横向排列 */
  gap: 20px; /* 各个 list-section 之间的间距 */
  flex-wrap: wrap; /* 如果空间不足则换行 */
}

.list-section {
  flex: 1; /* 每个 list-section 占据可用空间 */
  min-width: 300px; /* 每个 list-section 的最小宽度，确保内容不会过窄 */
  margin-bottom: 30px;
  display: flex; /* 使 h2 和 list-group 垂直排列 */
  flex-direction: column; /* 使 h2 和 list-group 垂直排列 */
}

.list-section .list-group {
  display: flex; 
  flex-direction: column; /* 列表项垂直排列 */
  gap: 10px; /* 列表项之间的间隙 */
  width: 100%; /* 确保 list-group 占据其父容器的全部宽度 */
}

.list-group-item {
  background-color: #fff; /* 卡片背景 */
  border: 1px solid #e9ecef; /* 更浅的边框 */
  border-radius: 8px;
  padding: 15px 20px; /* 调整内边距 */
  transition: box-shadow 0.2s ease-in-out, transform 0.2s ease-in-out;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 100%;
  box-sizing: border-box;
  position: relative; /* 为编辑按钮定位 */
}

/* 响应式调整：当屏幕较窄时，让 lists-container-horizontal 中的 list-section 垂直堆叠 */
@media (max-width: 1200px) { /* 可以根据实际效果调整断点 */
  .lists-container-horizontal {
    flex-direction: column;
  }
  .list-section {
    min-width: 100%; /* 垂直堆叠时，每个 section 占据全部宽度 */
  }
}

/* 原有的 list-group-item 媒体查询可能不再直接适用，因为它们是基于 list-group-item 横向排列的假设 */
/* 如果需要针对不同屏幕尺寸调整 list-group-item 内部布局，可以在这里添加新的规则 */

/*
@media (max-width: 992px) {
  .list-group-item {
    width: calc(50% - 7.5px); 
  }
}

@media (max-width: 768px) {
  .list-group-item {
    width: 100%; 
  }
}
*/

.list-group-item:hover {
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
  transform: translateY(-3px);
  border-color: #5e72e4;
}

.list-group-item .btn-edit {
  background-color: #5e72e4; /* 主题色 */
  color: white;
  border: none;
  border-radius: 5px;
  padding: 6px 12px;
  font-size: 13px;
  font-weight: 500;
  /* margin-right: 15px; */ /* 调整为绝对定位或flex布局控制 */
  transition: background-color 0.3s ease;
  position: absolute; /* 尝试将编辑按钮放在右上角 */
  top: 10px;
  right: 10px;
}

.list-group-item .btn-edit:hover {
  background-color: #4a5cc0; /* 主题色 hover */
}

.list-group-item span, .list-group-item a {
  margin-right: 10px;
  color: #495057;
  font-size: 14px;
  margin-bottom: 5px; /* 增加垂直间距 */
}

.list-group-item > *:not(.btn-edit) { /* 确保内容不与绝对定位的按钮重叠 */
  margin-right: 50px; /* 为编辑按钮留出空间 */
}

.list-group-item a {
  color: #5e72e4;
  text-decoration: none;
  font-weight: 500;
}

.list-group-item a:hover {
  text-decoration: underline;
  color: #4a5cc0;
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

</style>

<template>
  <WebHead />
  <div class="control-page-wrapper">
    <div class="content-container">
        <h1 class="page-title">管理面板</h1>
        <div class="row">
            <div class="col-sm-4">
                <h2 class="section-title">操作区域</h2>
                <div class="form-section">
                    <h3>集装箱</h3>
                    <span v-if="containerForm.containerid" class="editing-indicator">正在编辑: {{ containerForm.containerid }}</span>
                    <label class="form-label" for="containerTitle">名称</label>
                    <input type="text" id="containerTitle" v-model="containerForm.title" class="form-control">
                    <label class="form-label" for="containerInfo">描述</label>
                    <textarea id="containerInfo" v-model="containerForm.info" class="form-control"></textarea>
                    <div class="d-grid">
                        <button v-on:click="updateContainer()" class="btn-action">修改集装箱</button>
                    </div>
                    <div class="d-grid">
                        <button v-on:click="deleteContainer()" class="btn-action btn-delete">删除集装箱</button>
                    </div>
                </div>
                <div class="form-section">
                    <h3>公司</h3>
                    <span v-if="companyForm.companyid" class="editing-indicator">正在编辑: {{ companyForm.companyid }}</span>
                    <label class="form-label" for="companyName">公司全称</label>
                    <input type="text" id="companyName" v-model="companyForm.name" class="form-control">
                    <label class="form-label" for="companyInfo">描述</label>
                    <textarea id="companyInfo" v-model="companyForm.info" class="form-control"></textarea>
                    <div class="d-grid">
                        <button v-on:click="updateCompany()" class="btn-action">修改公司</button>
                    </div>
                    <div class="d-grid">
                        <button v-on:click="deleteCompany()" class="btn-action btn-delete">删除公司</button>
                    </div>
                </div>
                <div class="form-section">
                    <h3>用户</h3>
                    <span v-if="userForm.username" class="editing-indicator">正在编辑: {{ userForm.username }}</span>
                    <label class="form-label" for="userName">名称</label>
                    <input type="text" id="userName" v-model="userForm.name" class="form-control">
                    <label class="form-label" for="userInfo">介绍</label>
                    <input type="text" id="userInfo" v-model="userForm.info" class="form-control">
                    <label class="form-label" for="userType">类型</label>
                    <input type="text" id="userType" v-model="userForm.type" class="form-control">
                    <div class="d-grid">
                        <button v-on:click="updateUser()" class="btn-action">修改用户</button>
                    </div>
                    <div class="d-grid">
                        <button v-on:click="deleteUser()" class="btn-action btn-delete">删除用户</button>
                    </div>
                </div>
            </div>
            <div class="col-sm-8">
                <div class="lists-container-horizontal">
                    <div class="list-section">
                        <h2 class="section-title">集装箱列表</h2>
                        <div class="list-group">
                            <div v-for="item in containerArray" :key="item.containerid" class="list-group-item">
                                <button
                                    v-on:click="setContainerForm({
                                        'containerid':item.containerid,
                                        'title':item.title,
                                        'info': item.info,
                                    })"
                                    class="btn-edit"
                                >
                                    <i class="fas fa-edit"></i> 编辑
                                </button>
                                <RouterLink v-bind:to="'/container?containerid='+item.containerid">
                                    {{ item.title }}
                                </RouterLink>
                                <span>描述: {{ item.info }}</span>
                                <span v-if="!item.exittime">{{ toNormalDate(item.entertime) }}入库</span>
                                <span v-else>{{ toNormalDate(item.exittime) }}离库</span>
                            </div>
                        </div>
                    </div>
                    <div class="list-section">
                        <h2 class="section-title">公司列表</h2>
                        <div class="list-group">
                            <div v-for="item in companyArray" :key="item.companyid" class="list-group-item">
                                <button
                                    v-on:click="setCompanyForm({
                                        'companyid':item.companyid,
                                        'name':item.name,
                                        'info':item.info,
                                    })"
                                    class="btn-edit"
                                >
                                    <i class="fas fa-edit"></i> 编辑
                                </button>
                                <span>ID: {{ item.companyid }}</span>
                                <span>公司: {{ item.name }}</span>
                                <span>介绍: {{ item.info }}</span>
                            </div>
                        </div>
                    </div>
                    <div class="list-section">
                        <h2 class="section-title">用户列表</h2>
                        <div class="list-group">
                            <div v-for="item in userArray" :key="item.username" class="list-group-item">
                                <button
                                    v-on:click="setUserForm({
                                        'username':item.username,
                                        'name':item.name,
                                        'info':item.info,
                                        'type':item.type,
                                    })"
                                    class="btn-edit"
                                >
                                    <i class="fas fa-edit"></i> 编辑
                                </button>
                                <span>用户ID: {{ item.username }}</span>
                                <span>用户: {{ item.name }}</span>
                                <span>类型: {{ item.type }}</span>
                                <span>介绍: {{ item.info }}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
      </div>
    </div>
  <WebFooter />
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

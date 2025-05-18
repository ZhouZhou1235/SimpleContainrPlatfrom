<!-- 内容添加 -->

<script setup>
import { postRequest } from '@/api/HttpRequest';
import router from '@/router';
import { urls } from '@/vars/urls';
import WebFooter from '@/components/WebFooter.vue'; // 引入 WebFooter 组件

</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

.add-page-wrapper {
  padding-bottom: 70px; /* 为固定页脚预留空间 */
  display: flex;
  flex-direction: column; 
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px;
  font-family: 'Roboto', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  box-sizing: border-box;
}

.content-container {
  background-color: rgba(255, 255, 255, 0.95);
  padding: 30px 40px;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
  width: 100%;
  max-width: 900px; /* Adjusted for potentially wider forms */
  margin-top: 20px;
  margin-bottom: 20px;
  backdrop-filter: blur(5px);
  text-align: left;
}

.section-title {
  font-size: 24px;
  color: #333;
  margin-bottom: 25px;
  font-weight: 700;
  border-bottom: 2px solid #5e72e4;
  padding-bottom: 10px;
  display: inline-block;
}

.form-section {
  margin-bottom: 40px;
}

.form-section h3 {
  font-size: 20px;
  color: #495057;
  margin-bottom: 20px;
  font-weight: 600;
}

.form-label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: #495057;
  font-size: 14px;
}

.form-control {
  width: 100%;
  padding: 12px 15px;
  border: 1px solid #ced4da;
  border-radius: 6px;
  box-sizing: border-box;
  font-size: 15px;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
  background-color: #f8f9fa;
  margin-bottom: 15px; /* Add some space below each form control */
}

.form-control::placeholder {
  color: #adb5bd;
}

.form-control:focus {
  border-color: #5e72e4;
  outline: none;
  box-shadow: 0 0 0 3px rgba(94, 114, 228, 0.25);
  background-color: #fff;
}

textarea.form-control {
  min-height: 100px; /* Ensure textareas have a decent default height */
  resize: vertical; /* Allow vertical resizing */
}

.btn-submit {
  width: 100%;
  padding: 12px;
  background-color: #5e72e4;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 17px;
  font-weight: 600;
  transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.2s ease;
  margin-top: 10px; /* Space above the button */
  letter-spacing: 0.5px;
}

.btn-submit:hover {
  background-color: #4a5cc0;
  box-shadow: 0 4px 15px rgba(94, 114, 228, 0.35);
}

.btn-submit:active {
  transform: translateY(2px);
  box-shadow: 0 2px 8px rgba(94, 114, 228, 0.3);
}

.info-text p {
  font-size: 14px;
  color: #6c757d;
  background-color: #e9ecef;
  padding: 10px;
  border-radius: 6px;
  margin-bottom: 15px;
  line-height: 1.6;
}

/* Adjust Bootstrap default padding if necessary, or use custom classes */
.p-3 {
  padding: 1.5rem !important;
}

</style>

<template>
  <WebHead />
  <div class="add-page-wrapper">
    <div class="content-container">
        <div class="p-3 form-section">
            <h2 class="section-title">添加集装箱</h2>
            <div class="row">
                <div class="col-sm-6">
                    <h3>集装箱信息</h3>
                    <label class="form-label" for="containerCompanyId">公司ID</label>
                    <input type="text" id="containerCompanyId" v-model="containerForm.companyid" class="form-control">
                    <label class="form-label" for="containerTitle">名称</label>
                    <input type="text" id="containerTitle" v-model="containerForm.title" class="form-control">
                    <label class="form-label" for="containerInfo">描述</label>
                    <textarea id="containerInfo" v-model="containerForm.info" class="form-control"></textarea>
                </div>
                <div class="col-sm-6">
                    <div>
                        <h3>货物详情</h3>
                        <div class="info-text">
                          <p>
                              输入格式示例：<br>
                              苹果 100<br>
                              香蕉 200<br>
                              ...
                          </p>
                        </div>
                        <label class="form-label" for="cargoText">货物列表</label>
                        <textarea id="cargoText" v-model="containerForm.cargoText" class="form-control" rows="4"></textarea>
                    </div>
                    <div class="d-grid mt-3">
                        <button v-on:click="addContainer()" class="btn-submit">添加集装箱</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="p-3 form-section">
            <h2 class="section-title">添加公司</h2>
            <label class="form-label" for="companyName">公司全称</label>
            <input type="text" id="companyName" v-model="companyForm.name" class="form-control">
            <label class="form-label" for="companyInfo">描述</label>
            <textarea id="companyInfo" v-model="companyForm.info" class="form-control" rows="4"></textarea>
            <div class="d-grid mt-3">
                <button v-on:click="addCompany()" class="btn-submit">添加公司</button>
            </div>
        </div>
      </div>
    </div>
  <WebFooter />
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

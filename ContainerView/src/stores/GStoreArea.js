// pinia状态管理
// 应用的全局空间

import { getRequest, postRequest } from '@/api/HttpRequest';
import { urls } from '@/vars/urls';
import { defineStore } from 'pinia'

export const GStoreArea = defineStore('GStoreArea',{
    state:()=>{
        const user = {
            isLog: false,
            username: null,
            name: null,
            type: null,
        };
        const admin = {
            isLog: false,
            admin: null,
            name: null,
        };
        return {user,admin}
    },
    actions: {
        setUserData(data){
            if(data!=undefined){
                this.user.username = data[0].username;
                this.user.name = data[0].name;
                this.user.type = data[0].type;
                this.user.isLog = true;
            }
        },
        setAdminData(data){
            this.admin.admin = data[0].admin;
            this.admin.name = data[0].name;
            this.admin.isLog = true;
        },
        getAndSetUser(username=""){
            // 存在session的检查登录
            if(username==""){
                postRequest(urls.checkLogin).then(res=>{
                    if(res){
                        getRequest(urls.getUser).then(res=>{
                            let data = res.data;
                            this.setUserData(data);
                        });
                    }
                });
            }
            // 登录动作
            else{
                getRequest(urls.getUser+username).then(res=>{
                    if(res){
                        let data = res.data;
                        this.setUserData(data);
                    }
                });    
            }
        },
        getAndSetAdmin(){
            getRequest(urls.getAdmin).then(res=>{
                if(res!='no data'){
                    let data = res.data;
                    this.setAdminData(data);
                }
            });
        },
    }
});

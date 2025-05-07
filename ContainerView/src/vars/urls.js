// 请求地址

import { GArea } from "@/vars/ConstVar";

export const urls = {
    logout:GArea.proxyURL+'/logout',
    getUser:GArea.proxyURL+'/getUser?username=',
    doLogin:GArea.proxyURL+'/dologin',
    checkLogin:GArea.proxyURL+'/checkLogin',
    getContainers:GArea.proxyURL+'/getContainers',
    addContainer:GArea.proxyURL+'/addContainer',
    doRegister:GArea.proxyURL+'/doRegister',
    addCompany:GArea.proxyURL+'/addCompany',
    getContainerByUsername:GArea.proxyURL+'/getContainerByUsername?username=',
    containerExit:GArea.proxyURL+'/containerExit',
    adminDologin:GArea.proxyURL+'/adminDologin',
    getAdmin:GArea.proxyURL+'/getAdmin',
    getContainerFull:GArea.proxyURL+'/getContainerFull?containerid=',
    getCompanys:GArea.proxyURL+'/getCompanys',
    getUsers:GArea.proxyURL+'/getUsers',
    updateContainer:GArea.proxyURL+'/updateContainer',
    updateCompany:GArea.proxyURL+'/updateCompany',
    updateUser:GArea.proxyURL+'/updateUser',
    deleteContainer:GArea.proxyURL+'/deleteContainer',
    deleteCompany:GArea.proxyURL+'/deleteCompany',
    deleteUser:GArea.proxyURL+'/deleteUser',
};

// HTTP 请求

import axios from "axios";
import { GArea } from "@/vars/ConstVar";

// get请求
export async function getRequest(url=GArea.connectURL){
    let echoThing = null;
    await axios
    .get(url)
    .then(res=>{echoThing=res.data});
    return echoThing;
};

// post请求
export async function postRequest(url=GArea.connectURL,obj={},header={}){
    // {headers: {'Content-Type':'mutipart/form-data'}}
    let params = new FormData();
    for(let key in obj){params.append(key,obj[key])};
    let echoThing = null;
    await axios
    .post(url,params,header)
    .then(res=>{echoThing=res.data});
    return echoThing;
}

<!-- 根组件 -->

<script setup>
    import { RouterView } from 'vue-router'
    import WebHead from './components/WebHead.vue';
    import WebFooter from './components/WebFooter.vue';
    import { GStoreArea } from './stores/GStoreArea';
</script>

<template>
    <WebHead></WebHead>
    <RouterView/>
    <WebFooter></WebFooter>
</template>

<script>
    export default {
        mounted(){
            let GStore = GStoreArea();
            GStore.getAndSetUser();
            GStore.getAndSetAdmin();
        },
    }
</script>

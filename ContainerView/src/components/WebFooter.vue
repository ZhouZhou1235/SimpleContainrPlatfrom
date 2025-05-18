<template>
  <footer class="web-footer">
    <div class="container text-center">
      <small>集装箱平台 - 数据库航运课程设计</small>
    </div>
  </footer>
</template>

<style scoped>
.web-footer {
  background-color: #2c3e50; /* 与 global.css 中的 --primary 颜色一致或相近 */
  color: #ecf0f1; /* 浅色文字以搭配深色背景 */
  padding: 15px 0;
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  z-index: 1000; /*确保在最上层*/
  box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
}

.web-footer small {
  font-size: 0.9em;
}
</style>

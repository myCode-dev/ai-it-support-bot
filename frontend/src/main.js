import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import "normalize.css"; // ✨ 全局引入 normalize.css
import "./assets/style.css"; // 你的全局樣式

const app = createApp(App);
app.use(router);
app.use(ElementPlus);
app.mount("#app");

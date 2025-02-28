import { createRouter, createWebHistory } from "vue-router";
import Layout from "../layouts/Layout.vue";
import ChatPage from "../views/ChatPage.vue";
import ItSupportPage from "../views/ItSupportPage.vue";
import NewTicket from "../views/NewTicket.vue";
import LoginPage from "../views/LoginPage.vue";

const routes = [
  { path: "/login", component: LoginPage },
  {
    path: "/",
    component: Layout, // 🟢 所有內頁都會包含 Layout
    children: [
      { path: "", component: ChatPage },
      { path: "it-support", component: ItSupportPage },
      { path: "new-ticket", component: NewTicket }
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;

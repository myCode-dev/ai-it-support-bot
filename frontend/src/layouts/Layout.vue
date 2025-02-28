<template>
    <div class="layout">
      <!-- 📌 Sidebar 側邊欄 -->
      <el-menu class="sidebar" :default-active="route.path" router>
        <el-menu-item index="/">🏠 FAQ</el-menu-item>
        <el-menu-item index="/it-support">💼 My Ticket</el-menu-item>
        <el-menu-item @click="logout">🚪 Logout</el-menu-item>
      </el-menu>
  
      <div class="main-content">
        <!-- 📌 Header 頁首 -->
        <header class="header">
          <h1>AI IT Support System</h1>
        </header>
  
        <!-- 📌 頁面內容 -->
        <div class="content">
          <router-view />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { useRouter, useRoute } from "vue-router";
  
  const router = useRouter();
  const route = useRoute();
  
  const logout = () => {
    localStorage.removeItem("user");
    router.push("/login");
  };
  </script>
  
  <style scoped>
  /* 📌 整體布局 */
  .layout {
    display: flex;
    height: 100vh;
  }
  
  /* 📌 側邊欄 */
  .sidebar {
    width: 200px;
    height: 100vh;
    background-color: #2c3e50;
    color: white; 
    padding-top: 20px;
  }

  .el-menu-item {
    color: white;
  }
  
  /* 📌 主要內容區域 */
  .main-content {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
  }
  
  /* 📌 頁首 */
  .header {
    background-color: #409eff;
    padding: 10px;
    text-align: center;
    color: white;
  }
  
  /* 📌 內部內容 */
  .content {
    padding: 20px;
    flex-grow: 1;
  }

  
  </style>
  
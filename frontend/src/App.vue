<template>
  <router-view />
</template>

<script setup>
import { computed } from "vue";
import { useRoute } from "vue-router";
import Layout from "./layouts/Layout.vue";

const route = useRoute();
const isLoggedIn = computed(() => localStorage.getItem("user") && route.path !== "/login");
</script>

<style scoped>
/* ✅ 讓 #app 撐滿整個畫面 */
#app {
  width: 100%;
  height: 100%;
}
</style>

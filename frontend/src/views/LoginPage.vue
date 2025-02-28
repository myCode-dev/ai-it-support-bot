<template>
  <div class="login-container">
    <el-card class="login-card">
      <h2>🔑 Login</h2>
      <el-form @submit.prevent="login">
        <el-form-item label="Username">
          <el-input v-model="username" required></el-input>
        </el-form-item>

        <el-form-item label="Password">
          <el-input type="password" v-model="password" required></el-input>
        </el-form-item>

        <el-button type="primary" @click="login">Login</el-button>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const username = ref("");
const password = ref("");

const login = () => {
  if (username.value && password.value) {
    localStorage.setItem("user", username.value);
    router.push("/");
  } else {
    alert("❌ Please enter valid credentials.");
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}

.login-card {
  width: 350px;
  text-align: center;
}
</style>

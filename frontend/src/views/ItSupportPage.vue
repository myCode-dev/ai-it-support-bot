<template>
  <div class="ticket-container">
    <div class="header">
      <h2>📋 My Tickets</h2>
      <el-button type="primary" @click="goToNewTicket">➕ New Ticket</el-button>
    </div>
    
    <!-- tickets list -->
    <el-table :data="tickets" style="width: 100%">
      <el-table-column prop="ticket_id" label="Ticket ID" width="100"></el-table-column>
      <el-table-column prop="issue" label="Issue"></el-table-column>
      <el-table-column prop="status" label="Status" width="120"></el-table-column>
    </el-table>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const tickets = ref([]);
const router = useRouter(); 
const fetchTickets = async () => {
  try {
    const res = await axios.get(`${import.meta.env.VITE_API_BASE_URL}/tickets`, {
      params: { user_id: "user123" }
    });
    tickets.value = res.data;
  } catch (error) {
    console.error("Error fetching tickets:", error);
  }
};

const goToNewTicket = () => {
  router.push("/new-ticket");
};

onMounted(fetchTickets);
</script>

<style scoped>
.ticket-container {
  max-width: 800px;
  margin: 50px auto;
  text-align: center;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.el-table {
  margin-bottom: 20px;
}
</style>

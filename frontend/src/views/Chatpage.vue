<template>
    <!-- <div class="chat-container"> -->
      <div class="chat-box">
        <div v-for="(msg, index) in messages" :key="index" :class="['message-wrapper', msg.sender]">
          <img :src="msg.sender === 'bot' ? botAvatar : userAvatar" class="avatar" />
          <div class="message">
            <p class="message-text">{{ msg.text }}</p>
            <button v-if="msg.sender === 'bot' && !msg.helpRequested && msg.text !== 'Hello! How can I assist you today?'" 
              class="no-help-btn" 
              @click="requestItSupport(index)">
              ❌ This didn’t help
            </button>
          </div>
        </div>
      </div>
  
      <!-- input area -->
      <div class="input-container">
        <input v-model="message" placeholder="Ask something..." @keyup.enter="askChatbot" />
        <button @click="askChatbot">➤</button>
      </div>
    <!-- </div> -->

    
  </template>
  
  <script setup>
  import { ref } from "vue";
  import axios from "axios";
  import botAvatarImg from "../assets/bot.png";
  import userAvatarImg from "../assets/user.png";
  import { ElMessageBox } from "element-plus";
  import { useRouter } from "vue-router";
  const router = useRouter();
  
  const message = ref("");
  const messages = ref([
    { text: "Hello! How can I assist you today?", sender: "bot", helpRequested: false }
  ]);

  const botAvatar = botAvatarImg;
  const userAvatar = userAvatarImg;
  

  
  const askChatbot = async () => {
    if (!message.value.trim()) return;
    messages.value.push({ text: message.value, sender: "user" });
    const userInput = message.value;
    message.value = "";
  
    try {
      const res = await axios.post(`${import.meta.env.VITE_API_BASE_URL}/chat`, {
        user_id: "user123",
        message: userInput
      });
  
      if (!res.data || !res.data.response) {
        throw new Error("Invalid API response");
      }
  
      messages.value.push({
        text: res.data.response,
        sender: "bot",
        helpRequested: false
      });
  
    } catch (error) {
      console.error("API Error:", error);
      messages.value.push({ text: "Error fetching response.", sender: "bot" });
    }
  };

const requestItSupport = (index) => {
  messages.value[index].helpRequested = true;  

  ElMessageBox.confirm(
    "This response didn't help. Would you like to contact IT Support?",
    "Need More Help?",
    {
      confirmButtonText: "Yes, Contact IT Support",
      cancelButtonText: "No, I'll try again",
      type: "warning"
    }
  )
    .then(() => {
      console.log("Redirecting to IT Support page...");
      router.push("/new-ticket");
    })
    .catch(() => {
      console.log("User chose not to contact IT Support.");
    });
};

  </script>
  
  <style scoped>
  .chat-container {
    display: flex;
    flex-direction: column;
    height: 100vh; 
    width: 100%;
    padding: 20px;
    background: #f5f5f5;
  }

  .chat-box {
    flex-grow: 1;
    overflow-y: auto;
    padding: 15px;
    border-radius: 10px;
    background: white;
    height: 65vh;
    display: flex;
    flex-direction: column;
  }
  
  .message-wrapper {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }

  .user {
    justify-content: flex-end;
  }
  
  .bot {
    justify-content: flex-start;
  }
  
  .avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin: 5px;
  }

  .message {
    max-width: 75%;
    padding: 12px;
    border-radius: 12px;
  }
  
  .user .message {
    background: #007bff;
    color: white;
    text-align: right;
    border-top-right-radius: 0;
  }

  .bot .message {
    background: #e5e5e5;
    color: black;
    text-align: left;
    border-top-left-radius: 0;
  }

  .input-container {
    display: flex;
    padding: 10px;
    background: white;
    border-top: 1px solid #ddd;
  }

  input {
    flex-grow: 1;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
  }

  button {
    margin-left: 10px;
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    cursor: pointer;
  }
 
  .no-help-btn {
    background-color: gray;
    color: white;
    font-size: 12px;
    border: none;
    cursor: pointer;
    padding: 5px;
    margin-top: 5px;
  }
  </style>
  
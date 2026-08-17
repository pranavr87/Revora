import axios from "axios";

const api = axios.create({
  baseURL: "https://revora-8kzq.onrender.com"
});

export default api;
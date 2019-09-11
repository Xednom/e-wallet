<template>
  <div v-if="users" class="container">
    <div class="card text-center profile-card">
      <div class="card-header">Profile tab</div>
      <div class="card-body">
        <div v-for="user in users" :key="user">
          <h5 class="card-title">Name: {{ user.first_name }} {{ user.last_name }}</h5>
        <p class="card-text">Email Address: {{ user.email_address }}</p>
        <p class="card-text">Address: {{ user.address }}</p>
        <p class="card-text">Country: {{ user.country }}</p>
        <p class="card-text">State: {{ user.state }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "Profile",
  data() {
    return {
      users: [],
      error: null,
      loading: false,
      fetching: false,
      next: null
    };
  },
  methods: {
    getUserData() {
      this.loading = true;
      let endpoint = `/api/v1/user/`;
      apiService(endpoint).then(data => {
        this.users.push(...data.results);
        this.loading = false;
      })
    }    
  },
  created() {
    this.getUserData();
  }
};
</script>

<style>
.profile-card{
  margin: 25px 0 0 0;
}
</style>
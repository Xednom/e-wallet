<template>
  <div class="home">
    <div class="container">
      <div class="card wallet-transactions">
        <h5 class="card-header">Wallet Transactions</h5>
        <div class="card-body">
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Date</th>
                <th scope="col">Card Type</th>
                <th scope="col">Amount Added</th>
                <th scope="col">Amount Deducted</th>
                <th scope="col">Total Amount</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="cash in cashes" :key="cash">
                <td>{{ cash.date }}</td>
                <td>{{ cash.card_type }}</td>
                <td>{{ Number(cash.amount_added).toLocaleString() }}</td>
                <td>{{ Number(cash.amount_deducted).toLocaleString() }}</td>
                <td>{{ Number(cash.total_amount).toLocaleString() }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { apiService } from "@/common/api.service.js"
export default {
  name: "home",
  data() {
    return {
      cashes: [],
      loading: false
    }
  },
  methods: {
    getTransaction() {
      this.loading = true;
      let endpoint = `/api/v1/cash/`
      apiService(endpoint)
      .then(data => {
        this.cashes.push(...data.results);
        this.loading = false;
      })
      .catch(err => {
        console.log(err);
      })
    }
  },
  created() {
    this.getTransaction();
  }
};
</script>
<style>
.wallet-transactions {
  margin: 20px 0 0 0;
}
</style>

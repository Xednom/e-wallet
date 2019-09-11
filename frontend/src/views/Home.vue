<template>
  <div class="home">
    <div class="container">
      <div class="row">
        <div class="col-md-4 col-sm-12">
          <div class="card border-success mb-3 cash-in" style="max-width: 18rem;">
            <div class="card-header bg-transparent border-success">Total Amount Added</div>
            <div class="card-body text-success">
              <p class="card-text">&#8369;{{ totalAmountAdded }}</p>
            </div>
          </div>
        </div>
        <div class="col-md-4 col-sm-12">
          <div class="card border-warning mb-3 cash-in" style="max-width: 18rem;">
            <div class="card-header bg-transparent border-warning">Total Amount Deducated</div>
            <div class="card-body text-warning">
              <p class="card-text">&#8369;{{ totalAmountDeducted }}</p>
            </div>
          </div>
        </div>
        <div class="col-md-4 col-sm-12">
          <div class="card border-info mb-3 cash-in" style="max-width: 18rem;">
            <div class="card-header bg-transparent border-info">Total Amount</div>
            <div class="card-body text-info">
              <p v-for="cash in cashes" :key="cash"
              class="card-text">&#8369;{{ Number(cash.total_amount).toLocaleString() }}</p>
            </div>
          </div>
        </div>
      </div>
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
import { apiService } from "@/common/api.service.js";
export default {
  name: "home",
  data() {
    return {
      cashes: [],
      loading: false
    };
  },
  computed: {
    totalAmountAdded() {
      return this.cashes.reduce(function(sum, cashes) {
        return sum + parseFloat(cashes.amount_added);
      }, 0);
    },
    totalAmountDeducted() {
      return this.cashes.reduce(function(sum, cashes) {
        return sum + parseFloat(cashes.amount_deducted);
      }, 0);
    }
  },
  methods: {
    getTransaction() {
      this.loading = true;
      let endpoint = `/api/v1/cash/`;
      apiService(endpoint)
        .then(data => {
          this.cashes.push(...data.results);
          this.loading = false;
        })
        .catch(err => {
          console.log(err);
        });
    }
  },
  created() {
    this.getTransaction();
  }
};
</script>
<style>
.wallet-transactions,
.cash-in {
  margin: 20px 0 0 0;
}
</style>

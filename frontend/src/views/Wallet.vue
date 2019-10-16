<template>
  <div class="container">
    <div class="card wallet-cash-in border-info">
      <div class="card-header">Cash in</div>
      <div class="card-body text-info">
        <h5 class="card-title">Add Cash to your Wallet</h5>
        <form @submit.prevent="onSubmit">
          <div v-if="error" class="alert alert-danger" role="alert">{{ error }}</div>
          <div v-if="success" class="alert alert-success" role="alert">Successful cash in</div>
          <div class="form-group row offset-md-2">
            <label for="inputEmail3" class="col-sm-2 col-form-label">Card Number</label>
            <div class="col-md-4 col-sm-12">
              <input v-model="newCashIn.card_details" type="text" class="form-control" />
            </div>
          </div>
          <div class="form-group row offset-md-2">
            <label for="inputPassword3" class="col-sm-2 col-form-label">Card Type</label>
            <div class="col-md-2 col-sm-12">
              <select v-model="newCashIn.card_type" class="form-control">
                <option>Debit</option>
                <option>Credit</option>
              </select>
            </div>
          </div>
          <div class="form-group row offset-md-2">
            <label class="col-sm-2 col-form-label">Balance</label>
            <div class="col-md-2 col-sm-12" v-for="user in users" :key="user.id">
              <span class="d-block balance">{{ user.balance }}</span>
            </div>
          </div>
          <div class="form-group row offset-md-2">
            <label class="col-sm-2 col-form-label">Amount to be Added</label>
            <div class="col-md-2 col-sm-12">
              <input v-model="newCashIn.amount_added" type="text" class="form-control" />
            </div>
          </div>
          <div class="form-group row offset-md-2">
            <div class="col-sm-10">
              <div v-if="saving">
                <button type="button" class="btn btn-success btn-add">Saving...</button>
              </div>
              <div v-else>
                <button type="submit" class="btn btn-success btn-add">Add</button>
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "CashIn",
  data() {
    return {
      saving: false,
      loading: false,
      users: [],
      error: null,
      success: false,
      card_details: null,
      card_type: null,
      total_amount: null,
      balance: null,
      amount_added: null,
      newCashIn: {
        card_details: null,
        card_type: null,
        total_amount: null,
        balance: null,
        amount_added: null
      }
    };
  },
  methods: {
    onSubmit() {
      if (!this.newCashIn.card_details) {
        this.error = "You can't add without the card number.";
      } else if (!this.newCashIn.amount_added) {
        this.error = "Please provide amount to be added.";
      } else {
        this.loading = true;
        this.saving = true;
        let endpoint = "/api/v1/cash-create/";
        let method = "POST";
        apiService(endpoint, method, this.newCashIn)
          .then(() => {
            this.saving = false;
            this.success = true;
          })
          .catch(err => {
            console.log(err);
          });
      }
    },
    getBalance() {
      this.loading = true;
      let endpoint = `/api/v1/user/`;
      apiService(endpoint).then(data => {
        this.users.push(...data.results);
        this.loading = false;
      })
    }
  },
  created() {
    this.getBalance();
  }
};
</script>

<style>
.wallet-cash-in {
  margin: 100px 0 0 0;
}
.btn-add {
  border-radius: 0px;
}
.balance,
.card-number {
  background-color: #b9bdba;
  color: white;
  border-radius: 4px;
}
</style>
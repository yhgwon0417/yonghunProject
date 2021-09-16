<template>
  <div id="googleLogin">
    <GoogleLogin
      :params="params"
      :onSuccess="onSuccess"
      :onFailure="onFailure"
      :renderParams="renderParams"
    />
  </div>
</template>

<script>
import GoogleLogin from "vue-google-login";

export default {
  data() {
    return {
      params: {
        client_id: process.env.VUE_APP_GOOGLE,
      },
      // only needed if you want to render the button with the google ui
      renderParams: {
        width: 250,
        height: 50,
        longtitle: true,
      },
    };
  },
  components: {
    GoogleLogin,
  },
  methods: {
    onSuccess(googleUser) {
      const token = googleUser["Zb"]["access_token"];
      this.$emit("getToken", token);
    },
    onFailure(data) {
      console.log(data);
      console.log("failure");
    },
  },
  mounted() {},
};
</script>
<style></style>

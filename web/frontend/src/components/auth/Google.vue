<template>
  <div id="googleLogin">
    <GoogleLogin
      id="google"
      :params="params"
      :onSuccess="onSuccess"
      :onFailure="onFailure"
      ><img src="@/assets/images/google.png" width="45px;" height="45x;"/></GoogleLogin
    >
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
        width: 50,
        height: 50,
        longtitle: false,
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
<style>
#google {
  /* background-color: white; */
  border:none;
  
  
}
</style>

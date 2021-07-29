<template>
  <div id="app">
    <KakaoLogin api-key="b5d876aa01293b162e25dfdad5b312fc" image="kakao_login_btn_medium" :on-success="onSuccess" :on-failure="onFailure"/>
  </div>
</template>
<script>
import KakaoLogin from "vue-kakao-login";

export default {
  name: "App",
  components: {
    KakaoLogin,
  },
  methods: {
    onSuccess(data) {
      console.log(data);
      console.log("success");
      this.sendData(data);
    },
    onFailure(data) {
      console.log(data);
      console.log("failure");
    },
    sendData(data) {
      this.$emit("sendData", data);
    },
  },
};
</script>

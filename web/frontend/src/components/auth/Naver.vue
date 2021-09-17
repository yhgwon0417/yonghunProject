<template>
  <div>
    <div id="naver_id_login">
    </div>
  </div>
</template>

<script>

export default {
  mounted() {
    const url = this.$store.state.target.front + "/#/naverCallback"
    const client_id = process.env.VUE_APP_NAVER
    
    const naver_id_login = new window.naver_id_login(
      client_id,
      url
    );
    const state = naver_id_login.getUniqState();
    naver_id_login.setButton(4, 10, 60); // 버튼 설정
    naver_id_login.setState(state);
    // naver_id_login.setPopup(); // popup 설정을 위한 코드
    naver_id_login.init_naver_id_login();
  },
  methods: {
    
  },
};
</script>
<style>
#naver_id_login{
  /* border:1px solid grey;
  display:inline-block; */

}


</style>

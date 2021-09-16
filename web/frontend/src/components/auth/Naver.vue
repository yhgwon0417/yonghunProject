<template>
  <div>
    <div id="naver_id_login">
      <img
        src="@/assets/images/naver_login.png"
        width="300px;"
        height="50px;"
      />
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    const url = this.$store.state.target.front + "/#/naverCallback"
    const naver_id_login = new window.naver_id_login(
      "0lJPGodvjN6aXnN8Mn__",
      url
    );
    const state = naver_id_login.getUniqState();
    naver_id_login.setButton("green", 3, 65); // 버튼 설정
    naver_id_login.setState(state);
    // naver_id_login.setPopup(); // popup 설정을 위한 코드
    naver_id_login.init_naver_id_login();
  },
  methods: {
    
  },
};
</script>
<style>

</style>

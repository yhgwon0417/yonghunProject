<template>
  <div>
    <p>Naver Callback Page</p>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      access_token: "",
    };
  },
  methods: {
    login() {
      axios
        .post("http://localhost:8000/yonghun/account/naver/login/finish/", {
          access_token: this.access_token,
        })
        .then((response) => {
          this.$store.commit("updateToken", response.data.token);
          // get and set auth user
          const base = {
            baseURL:
              this.$store.state.target.api +
              this.$store.state.endpoints.baseUrl,
            headers: {
              // Set your Authorization to 'JWT', not Bearer!!!
              Authorization: `JWT ${this.$store.state.jwt}`,
              "Content-Type": "application/json",
            },
            xhrFields: {
              withCredentials: true,
            },
          };

          // Even though the authentication returned a user object that can be
          // decoded, we fetch it again. This way we aren't super dependant on
          // JWT and can plug in something else.

          const axiosInstance = axios.create(base);
          axiosInstance({
            url: "/user/",
            method: "get",
            params: {},
          }).then((response) => {
            this.$store.commit("setAuthUser", {
              authUser: response.data,
              isAuthenticated: true,
            });
            this.$router.push({ name: "Home" });
          });
        })
        .then(() => {
          // console.log(response);
        })
        .catch((error) => {
          alert("로그인이 실패했습니다.");
          console.log(error);
          console.debug(error);
          console.dir(error);
        });
    },
  },
  mounted() {
    const naver_id_login = new window.naver_id_login(
      "0lJPGodvjN6aXnN8Mn__",
      "http://localhost:8081/#/naverCallback"
    );
    this.access_token = naver_id_login.getAccessToken(); // 정상적 로그인이 된 경우 access token값 출력
    this.login();
  },
};
</script>

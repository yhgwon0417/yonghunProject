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
    };
  },
  mounted() {
    const url = this.$store.state.target.front + "/#/naverCallback"
    const naver_id_login = new window.naver_id_login(
      "0lJPGodvjN6aXnN8Mn__",
      url
    );
    const access_token = naver_id_login.getAccessToken(); // 정상적 로그인이 된 경우 access token값 출력
    this.get_token_from_naver(access_token);
  },
  methods: {
    get_token_from_naver(token) {
      axios
        .post(
          this.$store.state.target.api + this.$store.state.endpoints.naver,
          {
            access_token: token,
          }
        )
        .then((response) => {
          this.$store.commit("updateToken", response.data.token);
          // get and set auth user
        })
        .catch((error) => {
          console.log(error);
          console.debug(error);
          console.dir(error);
        });
        this.authenticate();
    },
    authenticate(){
      const base = {
        baseURL:
          this.$store.state.target.api + this.$store.state.endpoints.baseUrl,
        headers: {
          Authorization: `JWT ${this.$store.state.jwt}`,
          "Content-Type": "application/json",
        },
        xhrFields: {
          withCredentials: true,
        },
      };

      const axiosInstance = axios.create(base);
      axiosInstance({
        url: "/user/",
        method: "get",
        params: {},
      })
        .then((response) => {
          this.$store.commit("setAuthUser", {
            authUser: response.data,
            isAuthenticated: true,
          });
          this.$router.push({ name: "Home" });
        })
        .catch((error) => {
          alert("로그인이 실패했습니다.");
          console.log(error);
          console.debug(error);
          console.dir(error);
        });
    }
  },
};
</script>

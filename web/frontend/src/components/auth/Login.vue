<template lang="html">
  <div>
    <div id="log">YongHun.net</div>
    <div id="normal_form">
      <form class="login form">
        <div>
          <img src="@/assets/images/icons8-id-64.png" height="40px;" />
          &nbsp;&nbsp;&nbsp;
          <input
            v-model="email"
            type="text"
            placeholder="Email"
            autofocus="autofocus"
            maxlength="150"
            height="20px;"
            id="id_email"
          />
        </div>
        <div>
          <img src="@/assets/images/icons8-id-64.png" height="40px;" />
          <input
            v-model="password"
            type="password"
            placeholder="Password"
            id="id_password"
          />
        </div>
        <div>
          <img
            src="@/assets/images/login.png"
            height="40px;"
            @click.prevent="get_token_from_drf"
          />
        </div>
      </form>
    </div>

    <div id="social">
      <div>SNS 계정으로 간편하게 로그인 하세요.</div>
      <div id="kakao">
        <Kakao @getToken="get_token_from_kakao" />
      </div>
      <div id="naver">
        <Naver />
      </div>
      <div id="google"><Google @getToken="get_token_from_google" /></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Kakao from "./Kakao";
import Google from "./Google";
import Naver from "./Naver";
import instance from "../axios/interceptor";

export default {
  components: {
    Kakao,
    Google,
    Naver,
  },
  data() {
    return {
      url: "",
      email: "",
      password: "",
    };
  },
  methods: {
    authenticate() {
      const base = {
        baseURL:
          this.$store.state.target.api + this.$store.state.endpoints.baseUrl,
        timeout: 10000,
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
    },
    get_token_from_drf() {
      const payload = {
        email: this.email,
        password: this.password,
      };
      instance
        .post(this.$store.state.endpoints.obtainJWT, payload)
        .then((response) => {
          this.$store.commit("updateToken", response.data.token);
          // get and set auth user
        })
        .catch((error) => {
          alert("DRF 서버로 부터 토큰을 받아오지 못했습니다.");
          console.log(error);
          console.debug(error);
          console.dir(error);
        });
      this.authenticate();
    },

    get_token_from_kakao(token) {
      axios
        .post(
          this.$store.state.target.api + this.$store.state.endpoints.kakao,
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

    get_token_from_google(token) {
      axios
        .post(
          this.$store.state.target.api + this.$store.state.endpoints.google,
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
  },
};
</script>

<style lang="css">
#logo {
  background-color: rgb(0, 255, 55);
}
#normal_form {
  border: 1px solid black;
  padding: 10px 30%;
}

#social {
  padding: 10px;
  border: 1px solid black;
}

#kakao{
  padding:0.2%;
}
#naver{
  padding:0.2%;
}
#google{
  padding:0.2%;
}
</style>

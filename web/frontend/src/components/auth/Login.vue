<template lang="html">
  <div>
    <form class="login form">
      <div class="field">
        <label for="id_email">Email</label>
        <input
          v-model="email"
          type="text"
          placeholder="Email"
          autofocus="autofocus"
          maxlength="150"
          id="id_email"
        />
      </div>
      <div class="field">
        <label for="id_password">Password</label>

        <input
          v-model="password"
          type="password"
          placeholder="Password"
          id="id_password"
        />
      </div>
      <button
        @click.prevent="get_token_from_drf"
        class="button primary"
        type="submit"
      >
        Log In
      </button>
    </form>

    <div id="social">
      <Kakao @getToken="get_token_from_kakao" />
      <Naver />
      <Google @getToken="get_token_from_google" />
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
        timeout: 3000,
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

<style lang="css"></style>

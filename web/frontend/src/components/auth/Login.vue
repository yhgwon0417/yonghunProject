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
        @click.prevent="authenticate"
        class="button primary"
        type="submit"
      >
        Log In
      </button>
    </form>

    <div id="social">
      <Kakao @sendData="kakao" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Kakao from "./Kakao";
import instance from '../axios/interceptor';

export default {
  components: {
    Kakao,
  },
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    authenticate() {
      const payload = {
        email: this.email,
        password: this.password,
      };
      instance
        .post(this.$store.state.endpoints.obtainJWT, payload)
        .then((response) => {
          this.$store.commit("updateToken", response.data.token);
          // get and set auth user
          const base = {
            baseURL: this.$store.state.endpoints.baseUrl,
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
          const axiosInstance = instance.create(base);
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
        .catch((error) => {
          alert("로그인이 실패했습니다.");
          console.log(error);
          console.debug(error);
          console.dir(error);
        });
    },
    kakao(data) {
      instance
        .post(this.$store.state.endpoints.kakao, {
          access_token: data.access_token,
        })
        .then((response) => {
          this.$store.commit("updateToken", response.data.token);
          // get and set auth user
          const base = {
            baseURL: this.$store.state.endpoints.baseUrl,
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
        .catch((error) => {
          console.log(error);
          console.debug(error);
          console.dir(error);
        });
    },

  },
};
</script>

<style lang="css">
#social {
  border: 1px solid black;
}
</style>

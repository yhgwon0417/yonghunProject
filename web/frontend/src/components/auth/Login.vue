<template lang="html">
  <div id="layout">
    <div id="log"><img src="@/assets/images/ci.png" /></div>
    <div id="normal_form">
      <form class="login form">
        <div id="id">
          <input
            v-model="email"
            type="text"
            placeholder="Email"
            autofocus="autofocus"
            maxlength="150"
            height="30px;"
            id="id_email"
          />
        </div>
        <div id="passwd">
          <input
            v-model="password"
            type="password"
            placeholder="Password"
            id="id_password"
          />
        </div>
        <div id="login">
          <img
            src="@/assets/images/login.png"
            height="auto;"
            width="350px;"
            @click.prevent="get_token_from_drf"
          />
        </div>
      </form>
    </div>

    <div id="social">
      <div>SNS 계정으로 간편하게 로그인 하세요.</div>
      <Kakao id="kakao" @getToken="get_token_from_kakao" />
      <Naver id="naver" />
      <Google id="google" @getToken="get_token_from_google" />
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

#social {
  padding: 10px;
  border: 1px solid black;
  width: 350px;
  display: inline-block;
}

#layout {
  text-align: center;
}

input[type="text"],
input[type="password"] {
  -webkit-border-radius: 10px;
  -moz-border-radius: 10px;
  border-radius: 10px;
  border: 1px solid #2d9fd9;
  color: #a0d18c;
  width: 350px;
  height: 50px;
  padding-left: 10px;
}

input[type="text"]:focus {
  outline: none;
  border: 1px solid #a0d18c;
  color: #2d9fd9;
}
#id,
#password,
#login {
  padding: 10px;
}
#kakao,
#naver,
#google {
  display:inline-block;
}
</style>

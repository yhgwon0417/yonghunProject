import Vue from 'vue'
import Vuex from 'vuex';
import axios from 'axios';



Vue.use(Vuex);
// Make Axios play nice with Django CSRF
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default new Vuex.Store({
  state: {
    authUser: {},
    isAuthenticated: false,
    jwt: localStorage.getItem('token'),
    target:{
      front: process.env.VUE_APP_HOST + ":" + process.env.VUE_APP_PORT,
      api: process.env.VUE_APP_APIHOST + ":" + process.env.VUE_APP_APIPORT
    },
    endpoints: {
      // TODO: Remove hardcoding of dev endpoints
      obtainJWT: '/rest-auth/obtain_token/',
      refreshJWT: '/rest-auth/refresh_token/',
      logout: '/rest-auth/logout/',
      baseUrl: '/rest-auth/',
      kakao:"/yonghun/account/kakao/login/finish/",
      google:"/yonghun/account/google/login/finish/",
      naver:"/yonghun/account/naver/login/finish/"
    }
  },

  mutations: {
    setAuthUser(state, {
      authUser,
      isAuthenticated
    }) {
      Vue.set(state, 'authUser', authUser)
      Vue.set(state, 'isAuthenticated', isAuthenticated)
    },
    updateToken(state, newToken) {
      // TODO: For security purposes, take localStorage out of the project.
      localStorage.setItem('token', newToken);
      state.jwt = newToken;
    },
    removeToken(state) {
      // TODO: For security purposes, take localStorage out of the project.
      localStorage.removeItem('token');
      state.jwt = null;
    }
  }
})
import Vue from 'vue'
import App from './App.vue'
import axios from 'axios';
import router from './routes'; //설정 라우터 호출
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueMoment from 'vue-moment';
import VueTyperPlugin from 'vue-typer';



Vue.use(VueTyperPlugin)

Vue.use(VueMoment)

Vue.use(BootstrapVue)

Vue.config.productionTip = true;

Vue.prototype.$axios = axios; //전역변수로 설정 컴포넌트에서 this.$axios 호출할 수 있음

new Vue({
  render: h => h(App)
  ,router               //뷰에 설정
}).$mount('#app')
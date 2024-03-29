import Vue from "vue";
import Router from "vue-router";
import VueRouter from "vue-router";
import HelloWorld from "@/components/HelloWorld"; //메인 컴포넌트 호출
import List from "@/components/board/List"; //게시판 리스트 컴포넌트 호출
import Write from "@/components/board/Write"; //게시판 리스트 컴포넌트 호출
import View from "@/components/board/View";
import Profile_List from "@/components/profile/List";
import Certification from "@/components/profile/Certification";
import Technic from "@/components/profile/Technic";
import Login from "@/components/auth/Login";

Vue.use(Router); //vue 라우터 사용

const router = new VueRouter({
  routes: [
    {
      path: "/",
      name: HelloWorld,
      component: HelloWorld,
    },
  ],
});

router.beforeEach((to, from, next) => {
  alert(1);
  next();
});

export default new Router({
  //라우터 연결
  routes: [
    {
      path: "/",
      name: HelloWorld,
      component: HelloWorld,
    },
    {
      path: "/board/list",
      name: List,
      component: List,
    },
    {
      path: "/board/write",
      name: Write,
      component: Write,
    },
    {
      path: "/board/view", //상세페이지 추가
      name: View,
      component: View,
    },
    {
      path: "/profile/list", //상세페이지 추가
      name: Profile_List,
      component: Profile_List,
    },
    {
      path: "/profile/certification", //상세페이지 추가
      name: Certification,
      component: Certification,
    },
    {
      path: "/profile/technic", //상세페이지 추가
      name: Technic,
      component: Technic,
    },
    {
      path: "/auth/login", //상세페이지 추가
      name: Login,
      component: Login,
    },
  ],
});

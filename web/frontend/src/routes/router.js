import VueRouter from "vue-router";
import Vue from "vue";
import HelloWorld from "@/components/HelloWorld"; //메인 컴포넌트 호출

Vue.use(VueRouter);

export const router = new VueRouter({
  routes: [
    {
      path: "/test",
      name: HelloWorld,
      component: HelloWorld,
    },
  ],
});

router.beforeEach(function(to, from, next) {
  alert(1);
  next();
});

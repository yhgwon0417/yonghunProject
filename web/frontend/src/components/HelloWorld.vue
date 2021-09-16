<template>
  <div>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      controls
      indicators
      background="#ababab"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <!-- Text slides with image -->
      <b-carousel-slide
        caption="정보보안 컨설팅"
        text="웹, 모바일(Android, iOS) 모의해킹 전문가"
        img-src=""
      ></b-carousel-slide>

      <!-- Slides with custom text -->
      <b-carousel-slide
        caption="정보보안 교육"
        text="웹, 모바일(Android, iOS) 모의해킹 교육"
      >
        <template #img>
          <img
            class="d-block img-fluid w-100"
            width="1024"
            height="480"
            src=""
            alt="image slot"
          />
        </template>
      </b-carousel-slide>

      <!-- Slides with image only -->
      <b-carousel-slide
        caption="엄무자동화(RPA)"
        text="파이썬을 통합 업무자동화(한글, Word, Excel, Powerpoint)"
      >
        <template #img>
          <img
            class="d-block img-fluid w-100"
            width="1024"
            height="480"
            src=""
            alt="image slot"
          /> </template
      ></b-carousel-slide>

      <!-- Slides with img slot -->
      <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
      <b-carousel-slide
        caption="웹 개발"
        text="RestFul 웹 개발(Django Restful Framework, Vuejs)"
      >
        <template #img>
          <img
            class="d-block img-fluid w-100"
            width="1024"
            height="480"
            src="https://picsum.photos/1024/480/?image=55"
            alt="image slot"
          />
        </template>
      </b-carousel-slide>

      <!-- Slide with blank fluid image to maintain slide aspect ratio -->
      <b-carousel-slide
        caption="뭘 바"
      >
        <template #img>
          <img
            class="d-block img-fluid w-100"
            width="30"
            height="30"
            src=""
            alt="image slot"
        /></template>
        <p id="introduction">
          2018. 08. 정보처리기사<br />
          2020. 10. CISSP Associate<br />
          2020. 12. 정보보안기사<br />
          <!-- 2021. 12. CPPG(테스트 데이터)<br>
          2022. 02. ISMS-P 인증심사원(테스트 데이터) -->
        </p>
      </b-carousel-slide>
    </b-carousel>

    <p class="mt-4">
      Slide #: {{ slide }}<br />
      Sliding: {{ sliding }}
    </p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      slide: 0,
      sliding: null,
    };
  },
  methods: {
    onSlideStart() {
      this.sliding = true;
    },
    onSlideEnd() {
      this.sliding = false;
    },
  },
};
</script>
<style>
#introduction {
  text-align: left;
}
</style>

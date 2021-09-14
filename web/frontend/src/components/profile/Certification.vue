<template>
  <div>
    <h2>자격증</h2>
    <div class="accordion" role="tablist">
      <b-card no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-button block v-b-toggle.accordion-1 variant="info"
            >정보처리기사</b-button
          >
        </b-card-header>
        <b-collapse
          id="accordion-1"
          visible
          accordion="my-accordion"
          role="tabpanel"
        >
          <b-card-body>
            <b-card-text
              >I start opened because <code>visible</code> is
              <code>true</code></b-card-text
            >
            <b-card-text>{{ text }}</b-card-text>
          </b-card-body>
        </b-collapse>
      </b-card>

      <b-card no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-button block v-b-toggle.accordion-2 variant="info"
            >CISSP(Associate)</b-button
          >
        </b-card-header>
        <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
          <b-card-body>
            <b-card-text>{{ text }}</b-card-text>
          </b-card-body>
        </b-collapse>
      </b-card>

      <b-card no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-button block v-b-toggle.accordion-3 variant="info"
            >정보보안기사</b-button
          >
        </b-card-header>
        <b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
          <b-card-body>
            <b-card-text>{{ text }}</b-card-text>
          </b-card-body>
        </b-collapse>
      </b-card>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    //변수생성
    return {
      text: "test",
    };
  },
  mounted() {
    //페이지 시작하면은 자동 함수 실행
    this.fnGetList();
  },
  methods: {
    fnShowDetail(row) {
      return row.item.schedule_set;
    },

    fnGetList() {
      //데이터 가져오기 함수
      this.body = {
        // 데이터 전송
      };
      this.$axios
        .get("yonghun/company/list", {
          params: this.body,
        })
        .then((res) => {
          if (res.data.results) {
            this.results = res.data.results;
            // console.log(res.data);
            // this.paging = res.data.paging;
            // this.no = this.paging.totalCount - ((this.paging.page-1) * this.paging.ipp);
          } else {
            alert("실행중 실패했습니다.\n다시 이용해 주세요.");
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped></style>

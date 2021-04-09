<template>
  <div>
    <h2>자격증</h2>
    <div>
      <b-button v-b-toggle.collapse-1 variant="primary"
        >Toggle Collapse</b-button
      >
      <b-button v-b-toggle.collapse-2 variant="primary"
        >Toggle Collapse</b-button
      >
      <b-collapse id="collapse-1" class="mt-2">
        <b-card>
          <p class="card-text">Collapse contents Here</p>
        </b-card>
      </b-collapse>
      <b-collapse id="collapse-2" class="mt-2">
        <b-card>
          <p class="card-text">Collapse contents Here</p>
        </b-card>
      </b-collapse>
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
        .get("http://yonghun.net:8000/yonghun/company/list", {
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

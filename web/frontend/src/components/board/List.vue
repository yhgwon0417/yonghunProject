<template>
  <div>
    <h2>게시판 리스트</h2>
    <div class="form-inline my-2 my-lg-0">
      <input
        class="form-control mr-sm-2"
        type="text"
        placeholder="Search"
        v-model="search_term"
        aria-label="Search"
      />
      <button
        class="btn btn-outline-success my-2 my-sm-0"
        v-on:click.prevent="fnGetList()"
      >
        Search
      </button>
    </div>
    <div class="overflow-auto">
      <b-pagination
        v-model="offset"
        :total-rows="rows"
        :per-page="limit"
        aria-controls="my-table"
      ></b-pagination>

      <b-table
        :fields="fields"
        id="my-table"
        :items="list"
        :per-page="limit"
        :current-page="offset"
      >
        <template #cell(created_at)="data">
          {{ $moment(data.item.created_at).format("YYYY-MM-DD") }}
        </template>
        <template #cell(title)="data">
          <a href="#" v-on:click="fnView(`${data.item.id}`)">{{
            data.item.title
          }}</a>
        </template>
      </b-table>
      <div class="btnRightWrap">
        <a @click="fnAdd" class="btn">등록</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    //변수생성
    const fields = [
      { key: "id", label: "번호", sortable: true },
      { key: "created_at", label: "작성일", sortable: true },
      { key: "created_by", label: "작성자" },
      { key: "title", label: "제목" },
    ];
    return {
      limit: 10,
      offset: 0,
      rows: "",

      body: "", //리스트 페이지 데이터전송
      search_term: "",
      type: "", //게시판코드
      list: "", //리스트 데이터
      id: "",

      // fields
      fields: fields,
    };
  },
  mounted() {
    //페이지 시작하면은 자동 함수 실행
    this.fnGetList();
  },
  methods: {
    fnGetList() {
      //데이터 가져오기 함수
      this.body = {
        // 데이터 전송
        type: this.type,
        search_term: this.search_term,
        id: this.id,
      };
      this.$axios
        .get("http://localhost:8000/yonghun/blog/list/", { params: this.body })
        .then((res) => {
          if (res.data.results) {
            this.list = res.data.results;
            this.rows = res.data.count;
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
    fnAdd() {
      this.$router.push("./write");
    },
    fnView(index) {
      this.body.id = index;
      this.$router.push({ path: "./view", query: this.body }); //추가한 상세페이지 라우터
    },
  },
};
</script>

<style scoped>
.searchWrap {
  border: 1px solid #888;
  border-radius: 5px;
  text-align: center;
  padding: 20px 0;
  margin-bottom: 40px;
}
.searchWrap input {
  width: 60%;
  height: 36px;
  border-radius: 3px;
  padding: 0 10px;
  border: 1px solid #888;
}
.searchWrap .btnSearch {
  display: inline-block;
  margin-left: 10px;
}
.tbList th {
  border-top: 1px solid #888;
}
.tbList th,
.tbList td {
  border-bottom: 1px solid #eee;
  padding: 5px 0;
}
.tbList td.txt_left {
  text-align: left;
}
.btnRightWrap {
  text-align: right;
  margin: 10px 0 0 0;
}

.pagination {
  margin: 20px 0 0 0;
  text-align: center;
}
.first,
.prev,
.next,
.last {
  border: 1px solid #666;
  margin: 0 5px;
}
.pagination span {
  display: inline-block;
  padding: 0 5px;
  color: #333;
}
.pagination a {
  text-decoration: none;
  display: inline-blcok;
  padding: 0 5px;
  color: #666;
}
</style>

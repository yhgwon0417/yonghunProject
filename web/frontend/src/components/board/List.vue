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
        v-model="pagination.offset"
        :total-rows="pagination.rows"
        :per-page="pagination.limit"
        aria-controls="my-table"
      ></b-pagination>

      <b-table
        :fields="fields"
        id="my-table"
        :items="list"
        :per-page="pagination.limit"
        :current-page="pagination.offset"
      >
        <template #cell(type)="data">
          {{ data.item.type.name }}
        </template>
        <template #cell(created_at)="data">
          {{ $moment(data.item.created_at).format("YYYY-MM-DD") }}
        </template>
        <template #cell(title)="data">
          <a href="#" v-on:click="fnProcView(`${data.item.id}`)">{{
            data.item.title
          }}</a>
        </template>
      </b-table>
      <div class="btnRightWrap">
        <a @click="fnProcWrite" class="btn">등록</a>
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
      { key: "type", label: "분류", sortable: true },
      { key: "created_at", label: "작성일", sortable: true },
      { key: "created_by", label: "작성자" },
      { key: "title", label: "제목" },
    ];
    return {
      pagination: {
        limit: 10,
        offset: 0,
        rows: "",
      },

      form: {
        id: "",
        type: "",
        title: "",
        content: "",
      },
      search_term: "",

      list: "", //리스트 데이터

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
      this.$axios
        .get("http://yonghun.net:8000/yonghun/blog/list/")
        .then((res) => {
          if (res.data.results) {
            this.list = res.data.results;
            this.pagination.rows = res.data.count;
          } else {
            alert("실행중 실패했습니다.\n다시 이용해 주세요.");
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    fnProcWrite() {
      this.$router.push("./write");
    },
    fnProcView(id) {
      this.form.id = id;
      this.$router.push({ path: "./view", query: this.form }); //추가한 상세페이지 라우터
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

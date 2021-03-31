<template>
  <div>
    <h1>게시판 상세보기</h1>

    <div class="AddWrap">
      <form>
        <table class="tbAdd">
          <colgroup>
            <col width="15%" />
            <col width="*" />
          </colgroup>
          <tr>
            <th>제목</th>
            <td>{{ title }}</td>
          </tr>
          <tr>
            <th>내용</th>
            <td class="txt_cont" v-html="content"></td>
          </tr>
        </table>
      </form>
    </div>
    <div class="btnWrap">
      <a href="javascript:;" @click="fnMod" class="btn">수정</a>
    </div>
    <div class="btnWrap">
      <a href="javascript:;" @click="fnList" class="btn">목록</a>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      body: this.$route.query,
      title: "",
      content: "",
      view: "",
      id: this.$route.query.id,
    };
  },
  mounted() {
    this.fnGetView();
  },
  methods: {
    fnGetView() {
      this.$axios
        .get("http://localhost:8000/yonghun/blog/list/" + this.body.id)
        .then((res) => {
          this.title = res.data.title;
          this.content = res.data.content.replace(/(\n)/g, "<br/>");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    fnList() {
      delete this.body.num;
      this.$router.push({ path: "./list", query: this.body });
    },
  },
  fnMod() {
    this.$router.push({ path: "./wwrite", query: this.body });
  },
};
</script>

<style scoped>
.tbAdd {
  border-top: 1px solid #888;
}
.tbAdd th,
.tbAdd td {
  border-bottom: 1px solid #eee;
  padding: 5px 0;
}
.tbAdd td {
  padding: 10px 10px;
  box-sizing: border-box;
  text-align: left;
}
.tbAdd td.txt_cont {
  height: 300px;
  vertical-align: top;
}
.btnWrap {
  text-align: center;
  margin: 20px 0 0 0;
}
.btnWrap a {
  margin: 0 10px;
}
.btnAdd {
  background: #43b984;
}
.btnDelete {
  background: #f00;
}
</style>

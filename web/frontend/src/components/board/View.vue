<template>
  <div>
    <h1>게시판 상세보기</h1>

    <div class="AddWrap">
      <form>
        <table>
          <tr>
            <th>타입</th>
            <td>
              {{ type.name }}
            </td>
          </tr>
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
      <a href="javascript:;" @click="fnProcMod" class="btn">수정</a>
    </div>
    <div class="btnWrap">
      <a href="javascript:;" @click="fnDoDelete" class="btn">삭제</a>
    </div>
    <div class="btnWrap">
      <a href="javascript:;" @click="fnProcList" class="btn">목록</a>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      menuNum :"",
      form: this.$route.query,
      id: "",
      type: "",
      title: "",
      content: "",
    };
  },
  mounted() {
    this.fnGetView();
  },
  methods: {
    fnGetView() {
      this.$axios
        .get("http://yonghun.net:8000/yonghun/blog/list/" + this.form.id + "/")
        .then((res) => {
          (this.id = res.data.id), (this.type = res.data.type);
          this.title = res.data.title;
          this.content = res.data.content.replace(/(\n)/g, "<br/>");
        })
        .catch((err) => {
          console.log(err);
        });
    },

    fnProcList() {
      this.$router.push({ path: "./list" });
    },
    fnProcMod() {
      this.form.menuNum = 2;
      this.$router.push({ path: "./write", query: this.form });
      
    },
    fnDoDelete() {
      this.$axios
        .delete("http://yonghun.net:8000/yonghun/blog/list/" + this.id + "/")
        .then((res) => {
          alert("삭제되었습니다.");
          this.fnProcList();
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
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

<template>
  <div>
    <h1>게시판 상세보기</h1>

    <div class="AddWrap">
      <b-form-input
        id="input-2"
        v-model="type.name"
        required
        readonly
      ></b-form-input>
      <b-form-input
        id="input-2"
        v-model="title"
        placeholder="Title"
        required
        readonly
      ></b-form-input>
      <Tiptap @editorContent="editorContent" :value="content" readOnly></Tiptap>

      <div>
        <b-button-group>
          <b-button @click="fnProcMod" variant="primary">수정</b-button>
          <b-button @click="fnDoDelete" variant="primary">삭제</b-button>
          <b-button @click="fnProcList" variant="primary">목록</b-button>
        </b-button-group>
      </div>
    </div>
  </div>
</template>

<script>
import Tiptap from "../tiptap/Tiptap";
import instance from "../axios/interceptor";

export default {
  components: {
    Tiptap,
  },
  data() {
    return {
      menuNum: "",
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
      instance
        .get("yonghun/blog/list/" + this.form.id + "/")
        .then((res) => {
          
          this.id = res.data.id; 
          this.type = res.data.type;
          this.title = res.data.title;
          this.content = res.data.content.replace(/(\n)/g, "<br/>");
          // alert(this.content);
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
      instance
        .delete("yonghun/blog/list/" + this.id + "/")
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

<template>
  <div>
    <h1>게시판</h1>
    <b-form-select
      v-model="type"
      :options="options"
      class="mb-3"
      value-field="id"
      text-field="name"
      disabled-field="notEnabled"
    ></b-form-select>

    <b-form-group id="input-group-2" label="title:" label-for="input-2">
      <b-form-input
        id="input-2"
        v-model="title"
        placeholder="Enter name"
        required
      ></b-form-input>
    </b-form-group>

    <b-form-group id="input-group-2" label="content:" label-for="input-2">
      <b-form-textarea
        id="input-2"
        v-model="content"
        placeholder="Enter name"
        required
      ></b-form-textarea>
    </b-form-group>

    <b-button v-on:click="fnDoModify" variant="primary">Submit</b-button>
    <b-button v-on:click="fnDoDelete" variant="primary">Test</b-button>
  </div>
</template>

<script>
export default {
  data() {
    //변수 생성
    return {
      options: [],
      selected: "",
      id: "",
      type: "",
      title: "",
      content: "",
    };
  },
  mounted() {
    //페이지 시작하면은 자동 함수 실행
    this.fnGetType();
    this.fnPreWrite();
    // this.fnGetView();
  },

  methods: {
    fnList() {
      //리스트 화면으로 이동 함수
      this.$router.push({ path: "./list" });
    },
    fnGetType() {
      this.$axios
        .get("http://yonghun.net:8000/yonghun/type/list/")
        .then((res) => {
          this.options = res.data.results;
        })
        .then((err) => {
          console.log(err);
        });
    },
    fnGetView() {
      this.$axios
        .get("http://yonghun.net:8000/yonghun/blog/list/" + this.id + "/")
        .then((res) => {
          this.id = res.data.id;
          this.type = res.data.type.id;
          this.title = res.data.title;
          this.content = res.data.content;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    fnPreWrite() {
      if (this.$route.query.id) {
        this.id = this.$route.query.id;
        this.fnGetView();
      }
    },
  
    fnDoModify() {
      if (!this.title) {
        alert("제목을 입력해 주세요");
        this.$refs.title.focus(); //방식으로 선택자를 찾는다.
        return;
      }

      this.form = {
        type: this.type,
        title: this.title,
        content: this.content,
        id: this.id,
      };

      this.$axios
        .put("http://yonghun.net:8000/yonghun/blog/list/" + this.form.id + "/", {
          params: this.form,
          title: this.title,
          type: { id: 1, name: "모의해킹" },
        })
        .then((res) => {
          if (res.data) {
            alert("수정되었습니다.");
            this.fnList();
          } else {
            alert("실행중 실패했습니다.\n다시 이용해 주세요");
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    fnDoWrite() {
      //등록 프로세스

      if (!this.title) {
        //제목이 없다면 값을 입력하라고 알려준다.
        alert("제목을 입력해 주세요");
        this.$refs.title.focus(); //방식으로 선택자를 찾는다.
        return;
      }

      this.form = {
        //backend로 전송될 POST 데이터
        type: this.type,
        title: this.title,
        content: this.content,
      };

      this.$axios
        .post("http://yonghun.net:8000/yonghun/blog/list/", this.form)
        .then((res) => {
          if (res.data) {
            alert("등록되었습니다.");
            this.fnList();
          } else {
            alert("실행중 실패했습니다.\n다시 이용해 주세요");
          }
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
}
.tbAdd td input {
  width: 100%;
  min-height: 30px;
  box-sizing: border-box;
  padding: 0 10px;
}
.tbAdd td textarea {
  width: 100%;
  min-height: 300px;
  padding: 10px;
  box-sizing: border-box;
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

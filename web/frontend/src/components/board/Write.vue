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

    <Tiptap @editorContent="editorContent" :value="content"></Tiptap>

    <!-- <b-form-group id="input-group-2" label="content:" label-for="input-2">
      <b-form-textarea
        id="input-2"
        v-model="content"
        placeholder="Enter name"
        required
      ></b-form-textarea>
    </b-form-group> -->

    <div>
      <b-button-group>
        <b-button
          block
          v-on:click="fnDoWrite"
          v-if="this.menuNum == null"
          variant="primary"
          >등록</b-button
        >
        <b-button
          block
          v-on:click="fnDoModify"
          v-if="this.menuNum == 2"
          variant="primary"
          >수정</b-button
        >
      </b-button-group>
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
    //변수 생성
    return {
      options: [],
      selected: "",
      id: "",
      type: "",
      title: "",
      content: "",
      menuNum: this.$route.query.menuNum,
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
      instance
        .get("yonghun/type/list/")
        .then((res) => {
          this.options = res.data.results;
        })
        .then((err) => {
          console.log(err);
        });
    },
    fnGetView() {
      instance
        .get("yonghun/blog/list/" + this.id + "/")
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
      // console.log(this.options[0].name);
      // console.log(this.options[1].name);
      // console.log(this.options[2].name);

      this.form = {
        
        type: {
          id: this.type,
          name: "test"
        },
        title: this.title,
        content: this.content,
        id: this.id,
      };

      instance
        .put(
          "yonghun/blog/list/" + this.form.id + "/",

          this.form
        )
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
      if (!this.title) {
        //제목이 없다면 값을 입력하라고 알려준다.
        alert("제목을 입력해 주세요");
        this.$refs.title.focus(); //방식으로 선택자를 찾는다.
        return;
      }
      this.form = {
        //backend로 전송될 POST 데이터
        type: {
          id: this.type,
        },
        title: this.title,
        content: this.content,
      };
      console.log(this.form);
      instance
        .post("yonghun/blog/list/", this.form)
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
    editorContent(content) {
      console.log(content);
      this.content = content;
    },
  },
};
</script>

<style scoped></style>

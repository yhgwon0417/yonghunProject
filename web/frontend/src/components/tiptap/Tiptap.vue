<template>
  <div class="editor">
    <editor-menu-bar :editor="editor" v-slot="{ commands, isActive }">
      <div class="menubar">
        <button
          class="menubar__button"
          :class="{
            'v-btn--active': isActive.paragraph({ textAlign: 'left' }),
          }"
          @click="commands.paragraph({ textAlign: 'left' })"
        >
          L
        </button>
        <button
          class="menubar__button"
          :class="{
            'v-btn--active': isActive.paragraph({ textAlign: 'center' }),
          }"
          @click="commands.paragraph({ textAlign: 'center' })"
        >
          C
        </button>
        <button
          class="menubar__button"
          :class="{
            'v-btn--active': isActive.paragraph({ textAlign: 'right' }),
          }"
          @click="commands.paragraph({ textAlign: 'right' })"
        >
          R
        </button>

        <button
          class="menubar__button"
          @click="showImagePrompt(commands.image)"
        >
          <icon name="image" />
        </button>
        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.bold() }"
          @click="commands.bold"
        >
          B
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.italic() }"
          @click="commands.italic"
        >
          I
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.strike() }"
          @click="commands.strike"
        >
          S
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.underline() }"
          @click="commands.underline"
        >
          Underline
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.code() }"
          @click="commands.code"
        >
          Code
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.paragraph() }"
          @click="commands.paragraph"
        >
          Paragraph
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.heading({ level: 1 }) }"
          @click="commands.heading({ level: 1 })"
        >
          H1
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.heading({ level: 2 }) }"
          @click="commands.heading({ level: 2 })"
        >
          H2
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.heading({ level: 3 }) }"
          @click="commands.heading({ level: 3 })"
        >
          H3
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.bullet_list() }"
          @click="commands.bullet_list"
        >
          ul
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.ordered_list() }"
          @click="commands.ordered_list"
        >
          ol
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.blockquote() }"
          @click="commands.blockquote"
        >
          Quote
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.code_block() }"
          @click="commands.code_block"
        >
          code_block
        </button>

        <button class="menubar__button" @click="commands.horizontal_rule">
          horizontal_rule
        </button>

        <button class="menubar__button" @click="commands.undo">
          undo
        </button>

        <button class="menubar__button" @click="commands.redo">
          redo
        </button>
      </div>
    </editor-menu-bar>

    <editor-content class="editor__content" :editor="editor" />
  </div>
</template>

<script>
import Icon from "./Components/Icon";
import { Editor, EditorContent, EditorMenuBar } from "tiptap";
import {
  Blockquote,
  CodeBlock,
  HardBreak,
  Heading,
  OrderedList,
  BulletList,
  ListItem,
  TodoItem,
  TodoList,
  Bold,
  Code,
  Italic,
  Link,
  Strike,
  Underline,
  History,
  HorizontalRule,
  Image,
} from "tiptap-extensions";
import Iframe from "./Iframe.js";
import Paragraph from "./Paragraph.js";

export default {
  props: {
    value: String,
    readOnly: Boolean,
  },
  components: {
    EditorMenuBar,
    EditorContent,
    Icon,
  },

  data() {
    return {
      editor: new Editor({
        editable: !this.readOnly,
        extensions: [
          new Blockquote(),
          new BulletList(),
          new CodeBlock(),
          new HardBreak(),
          new Heading({ levels: [1, 2, 3] }),
          new HorizontalRule(),
          new ListItem(),
          new OrderedList(),
          new TodoItem(),
          new TodoList(),
          new Link(),
          new Bold(),
          new Code(),
          new Italic(),
          new Strike(),
          new Underline(),
          new History(),
          new Image(),
          new Iframe(),
          new Paragraph(),
        ],
        onUpdate: ({ getHTML }) => {
          this.$emit("editorContent", getHTML());
        },
      }),
    };
  },

  beforeMount() {},
  mounted() {},
  update() {},
  beforeDestroy() {
    this.editor.destroy();
  },
  watch: {
    value() {
      if (this.editor.getHTML() == "<p></p>" && this.value) {
        this.editor.setContent(this.value);
      }
    },
  },
  methods: {
    showImagePrompt(command) {
      const src = prompt("Enter the url of your image here");
      if (src !== null) {
        console.log(src);
        command({ src });
      }
    },
  },
};
</script>
<style scoped>
.editor {
  margin-top: 1em;
  border: 1px solid blanchedalmond;
}

.menubar {
  background-color: rgb(255, 251, 193);
}
.editor__content {
  border: 1px solid rgba(255, 251, 193);
}
</style>

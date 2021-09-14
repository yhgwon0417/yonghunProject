<template>
  <div>
    <h2>프로필</h2>
    <div>
      <b-table
        bordered
        striped
        hover
        :items="results"
        :fields="fields"
        @row-clicked="fnShowDetail"
      >
        <template #cell(name)="row">
          <div class="text-center">
            {{ row.item.name }}
            <b-badge variant="primary">1</b-badge>
          </div>
        </template>
        <template #cell(duration)="row"
          >{{ row.item.start_date }} ~ {{ row.item.end_date }}
        </template>
        <template #cell(show_details)="row">
          <b-button size="sm" @click="row.toggleDetails" class="mr-2">
            {{ row.detailsShowing ? "Hide" : "Show" }} Details
          </b-button>
        </template>

        <template #row-details="row">
          <b-card>
            <b-table
              striped
              hover
              :items="fnShowDetail(row)"
              :fields="fields_detail"
            >
              <template #cell(duration)="row">
                {{ row.item.start_date }}~{{ row.item.end_date }}
              </template>
              <template #cell(institution)="row">
                {{ row.item.institution }}
              </template>
              <template #cell(inspection_set)="row">
                <li v-for="value in row.item.inspection_set" :key="value.id">
                  {{ value.system }} {{ value.count }}
                </li>
              </template>
            </b-table>
            <b-button size="sm" @click="row.toggleDetails"
              >Hide Details</b-button
            >
          </b-card>
        </template>
      </b-table>
    </div>
  </div>
</template>

<script>
import instance from "../axios/interceptor";

export default {
  data() {
    //변수생성
    const fields = [
      { key: "id", label: "번호" },
      { key: "duration", label: "기간" },
      { key: "name", label: "회사명" },
      { key: "show_details", label: "세부사항" },
    ];

    const fields_detail = [
      { key: "id", label: "번호" },
      { key: "duration", label: "기간" },
      { key: "institution", label: "기관" },
      { key: "inspection_set", label: "대상" },
    ];

    return {
      body: "",
      results: "",
      fields: fields,
      fields_detail: fields_detail,
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
      this.body = {};

      instance
        .get("yonghun/company/list/", {
          params: this.body,
        })
        .then((res) => {
          if (res.data.results) {
            this.results = res.data.results;
          }
        })
        .catch((err) => {
          console.log(err);
          alert(
            "경력확인용 계정으로 로그인해야 합니다.(관리자에게 문의하세요)."
          );
        });
    },
  },
};
</script>

<style scoped></style>

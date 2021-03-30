<template>
	<div>
		<h2>게시판 리스트</h2>
		<div class="searchWrap">
			<input type="text" v-model="keyword" @keyup.enter="fnSearch" /><a href="javascript:;" @click="fnSearch" class="btnSearch btn">검색</a>
		</div>
		<div> 
			<b-table striped hover :items="list" :fields="fields">
				
			</b-table>
		</div>
		<div class="btnRightWrap">
			<a @click="fnAdd" class="btn">등록</a>
		</div>
	</div>
</template>

<script>
export default {
	
	data() { //변수생성
			const fields = [
			{ key: 'id', label: '번호' },
			{ key: 'created_by', label: '작성자' },
			{ key: 'created_at', label: '작성일'},
			{ key: 'title', label: '제목' },
			]		  
		return{
			body:'' //리스트 페이지 데이터전송
			,type:'' //게시판코드
			,list:'' //리스트 데이터
			,no:'' //게시판 숫자처리
			,paging:'' //페이징 데이터
			,start_page:'' //시작페이지
			,page:this.$route.query.page ? this.$route.query.page:1
			,keyword:this.$route.query.keyword
			,paginavigation:function() { //페이징 처리 for문 커스텀
				var pageNumber = [];
				var start_page = this.paging.start_page;
				var end_page = this.paging.end_page;
				for (var i = start_page; i <= end_page; i++) pageNumber.push(i);
				return pageNumber;
			},
			// fields
			fields: fields,
			
		}
	}
	,mounted() { //페이지 시작하면은 자동 함수 실행
		this.fnGetList();
	}
	, methods:{
		fnGetList() { //데이터 가져오기 함수
			this.body = { // 데이터 전송
				type:this.type
				,keyword:this.keyword
				,page:this.page
			}
			this.$axios.get('http://localhost:8000/yonghun/blog/list',{params:this.body})
			.then((res)=>{
				if(res.data.results) {
					this.list = res.data.results;
					// console.log(res.data);
					// this.paging = res.data.paging;
					// this.no = this.paging.totalCount - ((this.paging.page-1) * this.paging.ipp);
				} else {
					alert("실행중 실패했습니다.\n다시 이용해 주세요.");
				}
			})
			.catch((err)=>{
				console.log(err);
			})
		}
		,fnAdd() {
			this.$router.push("./write");
		}
		,getList() {
			this.$axios.get("http://localhost:8000/yonghun/blog/list")
			.then((res)=>{
				console.log(res);
			})
			.then((err)=>{
				console.log(err);
			})
		}
		,fnSearch() { //검색
			this.paging.page = 1;
			this.fnGetList();
		}
		, fnPage(n) {//페이징 이
			if(this.page != n) {
				this.page = n;
				this.fnGetList();
			}
		}
		, fnView(num) {
			this.body.num = num;
			this.$router.push({path:'./view',query:this.body}); //추가한 상세페이지 라우터
	}
	}
}
</script>

<style scoped>
	.searchWrap{border:1px solid #888; border-radius:5px; text-align:center; padding:20px 0; margin-bottom:40px;}
	.searchWrap input{width:60%; height:36px; border-radius:3px; padding:0 10px; border:1px solid #888;}
	.searchWrap .btnSearch{display:inline-block; margin-left:10px;}
	.tbList th{border-top:1px solid #888;}
	.tbList th, .tbList td{border-bottom:1px solid #eee; padding:5px 0;}
	.tbList td.txt_left{text-align:left;}
	.btnRightWrap{text-align:right; margin:10px 0 0 0;}

	.pagination{margin:20px 0 0 0; text-align:center;}
	.first, .prev, .next, .last{border:1px solid #666; margin:0 5px;}
	.pagination span{display:inline-block; padding:0 5px; color:#333;}
	.pagination a{text-decoration:none; display:inline-blcok; padding:0 5px; color:#666;}
</style>
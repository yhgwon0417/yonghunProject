<template>
  <header>
    <div>
      <b-navbar type="dark" variant="dark">
        <b-navbar-nav>
          <b-nav-item href="#"><router-link to="/">홈</router-link></b-nav-item>

          <!-- Navbar dropdowns -->
          <b-nav-item-dropdown text="프로필" left>
            <b-dropdown-item href="#"
              ><router-link to="/profile/list"
                >경력</router-link
              ></b-dropdown-item
            >
            <b-dropdown-item href="#"
              ><router-link to="/profile/certification"
                >자격증</router-link
              ></b-dropdown-item
            >
            <b-dropdown-item href="#"><router-link to="/profile/technic"
                >보유기술</router-link
              ></b-dropdown-item>
          </b-nav-item-dropdown>

          <b-nav-item-dropdown text="게시판" left>
            <b-dropdown-item href="#"
              ><router-link to="/board/list"
                >블로그</router-link
              ></b-dropdown-item
            >
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-navbar>
    </div>
  </header>
</template>

<script>
export default {};
</script>

<style scoped>
header {
  width: 100%;
  text-align: center;
  position: relative;
  height: 0.5%;
  background-color: rgb(234, 161, 48);
  border-bottom: 1px solid #35495e;
}
</style>

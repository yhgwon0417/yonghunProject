<template lang="html">
<div>
    

</div>

</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      
    }
  },
  mounted(){
    this.logout();
  },
  methods: {
        logout(){
          
      axios.get(this.$store.state.endpoints.logout)
        .then((response) =>{
          console.log(response);
          this.$store.state.isAuthenticated = false;
          this.$store.state.jwt = null;
          localStorage.removeItem('token')
          

        })
        .catch((error)=>{
          console.log(error);
        })
      
    },
  }
  
}
</script>

<style lang="css">
</style>
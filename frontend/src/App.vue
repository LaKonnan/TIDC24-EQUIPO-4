<template>
  <div id="app" v-if="$auth.isAuthenticated">
    <navbar v-if="!$auth.loading"/>
    <router-view/>
  </div>
</template>

<script>

export default {
  name: 'App',

  components: {
        'navbar': require('./components/Navbar.vue').default
    }
}
</script>

<style lang="scss">
  @import '@/components/styles/global.scss';
  body {  
    background: url('assets/background.png') fixed no-repeat bottom right !important;
    background-size: 50% !important;
  }
</style>
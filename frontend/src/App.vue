<template>
  <div id="app" v-if="$auth.isAuthenticated">
    <!-- v-if="!$auth.loading" -->
    <navbar />
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

<style>
  body {
    margin: 0;
    padding: 0;
    background-color:#f8f8f8!important;
  }
</style>
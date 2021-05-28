<template>
  <div>
    <!-- barra superior y lateral -->
    <navbar/>
    <div class="content">
      <br>
      <!-- titulo -->
      <p class="dark-title">GESTIÓN DE CAJAS CHICAS</p>
      <hr class="hr">
    </div>
  </div>

</template>

<script>

export default {
    name: 'cajas',
    data () {
        
    },
    components: {
        'navbar': require('../components/Navbar.vue').default
    }

}
</script>

<style>

</style>
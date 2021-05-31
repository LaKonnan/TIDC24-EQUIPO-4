<template>
  <div>
    <div class="content">
      <br>
      <!-- titulo -->
      <p class="dark-title">GESTIÓN DE CAJAS CHICAS</p>
      <hr class="hr">

      <!-- tabla de contenidos -->
      <table-cajas/>

      <!-- botones -->
      <buttons/>

    </div>
  </div>

</template>

<script>

export default {
    name: 'cajas',
    components: {
      'table-cajas': require('../components/cajas/all_table').default,
      'buttons': require('../components/cajas/buttons').default,
    }
}
</script>

<style>

</style>
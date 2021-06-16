<template>
  <div>
    <div class="content">
      <br>
      <!-- titulo -->
      <p class="dark-title">GESTIÓN DE CAJAS CHICAS</p>
      <hr class="hr">

      <!-- tabla de contenidos -->
      <table-cajas @items="rowItems"/>

      <!-- botones -->
      <buttons :items="items" />

    </div>
  </div>

</template>

<script>

export default {
    name: 'cajas',
    data() {
      return {
        items: []
      }
    },
    

    components: {
      'table-cajas': require('../components/cajas/all_table').default,
      'buttons': require('../components/cajas/buttons').default,
    },

    methods: {
      rowItems(params){
        this.items = params;
      }
    }
}
</script>

<style>

</style>
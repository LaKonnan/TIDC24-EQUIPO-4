<template>
  <div class="content">
    <br>

    <!-- resumen -->
    <resume />

    <!-- tabla de contenidos -->
    <table-cajas @items="rowItems" @row-selected="onRowSelected"/>

    <!-- botones -->
    <buttons :items="items" :selectedRow="selectedRow" />

  </div>
</template>

<script>

export default {
    name: 'cajas',
    data() {
      return {
        selectedRow: true,
        items: []
      }
    },
    
    // importar componentes de la pagina
    components: {
      'table-cajas': require('../components/cajas/all_table').default,
      'buttons': require('../components/cajas/buttons').default,
      'resume': require('../components/cajas/resumen_global').default
    },

    methods: {
      // fila seleccionada
      onRowSelected(params) {
        this.selectedRow = params
      },
      
      // datos de fila
      rowItems(params){
        this.items = params;
      }
    }
}
</script>

<style lang="scss">
  @import '@/components/styles/global.scss';
</style>
<template>
  <div class="content">
    <!-- tabla de contenidos -->
    <table-usuarios 
      ref="table-usuarios" 
      @row-selected="onRowSelected" 
      @items="rowItems"/>

    <!-- botones -->
    <buttons :table=table :selectedRow="selectedRow" :items="items"/>
  </div>
</template>

<script>

export default {
    name: 'usuarios',
    data(){
      return {
        selectedRow: true,
        items: [],
        table: null
      }
    },


    components: {
      'table-usuarios': require('../components/usuarios/tabla').default,
      'buttons': require('../components/usuarios/buttons').default
    },

    mounted(){
      this.table = this.$refs['table-usuarios']
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
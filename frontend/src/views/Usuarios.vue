<template>
  <div>
    <div class="content">
      <br>
      <!-- titulo -->
      <p class="dark-title">Gestión de usuarios</p>
      <hr class="hr">

      <!-- tabla de contenidos -->
      <table-usuarios ref="table-usuarios" @row-selected="onRowSelected" @items="rowItems"/>

      <!-- botones -->
      <buttons :table=table :selectedRow="selectedRow" :items="items"/>

    </div>
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
      onRowSelected(params) {
        this.selectedRow = params
      },
      rowItems(params){
        this.items = params;
      }
    }
}
</script>

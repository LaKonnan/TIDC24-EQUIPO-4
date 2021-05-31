<template>
    <div>
      <!-- tabla -->
      <b-table
        class = "table"
        selectable 
        :headers="header" 
        :items="cajas" 
        :select-mode="selectMode"
        :per-page="perPage"
        hover
        fixed
        responsive
        :current-page="currentPage">
      </b-table>

      <!-- paginado -->
      <b-pagination 
        v-model="currentPage" 
        :total-rows="rows" 
        :per-page="perPage" 
        aria-controls="my-table">
      </b-pagination>
  </div>
</template>

<script>
export default {
    data () {
        return {
            cajas: [],
            perPage: 10,
            selectMode: 'single',
            currentPage: 1,
            header: ['ID', 'ENCARGADO', 'ESTADO', 'MONTO DE GASTOS', 'MONTO TOTAL']
        }
    },

    created() {
        // obtener lista de obras
    },

    computed: {
        // obtener cantidad de elementos de cajas para paginado
        rows() {
            return this.cajas.length
        }
    }
}
</script>

<style>

</style>
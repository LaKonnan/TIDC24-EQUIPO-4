<template>
    <div>
      <!-- tabla -->
      <b-table
        class = "table"
        selectable 
        :items="maquinas" 
        :fields="fields"
        :select-mode="selectMode"
        :per-page="perPage"
        @row-selected="onRowSelected"
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
import { getAPI } from '../axios-api'

export default {
    data() {
      return  {
          maquinas: [],
          fields: [
              { key: 'id_maquina.S', label: 'RECURSO' },
              { key: 'patente.S', label: 'PATENTE' },
              { key: 'nombre.S', label: 'NOMBRE' },
              { key: 'ubicacion.N', label: 'UBICACIÓN' },
          ]
      }
    },

    created() {
        // obtener lista de maquinas
        getAPI.get('/maquinas',)
            .then(response => {
                this.maquinas = response.data
            })
    },

    computed: {
        rows() {
            return this.cajas.length
        }
    },

    methods: {
        onRowSelected(items) {
            this.$emit('items', items)
        }
    }
}
</script>

<style>

</style>
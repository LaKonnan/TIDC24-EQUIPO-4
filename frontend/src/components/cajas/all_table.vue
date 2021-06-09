<template>
    <div>
      <!-- tabla -->
      <b-table
        class = "table"
        selectable 
        :fields="header" 
        :items="cajas"
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
        

      {{ cajas }}
  </div>
</template>

<script>
import { getAPI } from '../axios-api'
export default {
    props: ['caja'],
    data () {
        return {
            cajas: [],
            perPage: 10,
            selectMode: 'single',
            currentPage: 1,
            selected: [],
            header: ['obraId', 'encargado', 'estado', 'nombre']
        }
    },

    created() {
        // obtener lista de obras
        getAPI.get('/cajas/OF53-01',)
                .then(response => {
                    console.log('Datos de caja recibidos')
                    this.cajas = response.data
                    console.log(this.cajas)
                })
                .catch(err => {
                    console.log(err)
                })
    },

    computed: {
        // obtener cantidad de elementos de cajas para paginado
        rows() {
            return this.cajas.length
        }
    },

    methods: {
        onRowSelected(items) {
            this.selected = items
            console.table(this.selected)
            
        }
        
    },
}
</script>

<style>

</style>
<template>
    <div>
      <!-- tabla -->
      <b-table
        class = "table"
        selectable 
        :headers="header" 
        :items="cajas" 
        :caja="caja"
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
import { getAPI } from '../axios-api'
export default {
    props: ['caja'],
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
        getAPI.get('/obras',)
                .then(response => {
                    console.log('Datos de caja recibidos')
                    this.cajas = response.data
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
    }
}
</script>

<style>

</style>
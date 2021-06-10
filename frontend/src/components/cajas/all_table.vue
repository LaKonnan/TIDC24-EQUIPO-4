<template>
    <div>
      <!-- tabla -->
      <b-table
        class = "table"
        selectable 
        :fields="fields" 
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
  </div>
</template>

<script>
import { getAPI } from '../axios-api'
export default {
    props: ['caja'],
    data () {
        return {
            cajas: [],
            test: [],
            perPage: 10,
            selectMode: 'single',
            currentPage: 1,
            selected: [],
            fields: [
                { key: 'id_caja.S', label: 'ID'},
                { key: 'tipo.S', label: 'TIPO'},
                { key: 'estado.S', label: 'ESTADO'},
                { key: 'monto_gastos.S', label: 'MONTO GASTOS'},
                { key: 'monto_total.S', label: 'MONTO TOTAL'}
            ]
        }
    },

    created() {
        // obtener lista de obras
        getAPI.get('/cajasChicas',)
            .then(response => {
                console.log('Datos de caja recibidos')
                this.cajas = response.data
                console.log(this.cajas)
                // this.cajas((a, b) => (a.id_caja> b.id_caja) ? 1 : -1)
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
            
        },       
    },
}
</script>

<style>

</style>
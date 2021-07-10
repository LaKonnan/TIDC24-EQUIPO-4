<template>
    <div>
      <!-- tabla -->
      <b-table
        class = "table table-responsive-sm"
        :fields="fields" 
        :items="cajas"
        :select-mode="selectMode"
        :per-page="perPage"
        @row-selected="onRowSelected"
        :current-page="currentPage"
        hover
        selectable 
        >
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
            selected: [],
            isSelected: false,

            // columnas con opcion a ordenar
            fields: [
                { key: 'id_caja.S', label: 'ID', sortable: true },
                { key: 'tipo.S', label: 'TIPO', sortable: true },
                { key: 'estado.S', label: 'ESTADO', sortable: true },
                { key: 'monto_gastos.S', label: 'MONTO GASTOS', sortable: true },
                { key: 'monto_total.S', label: 'MONTO TOTAL',  sortable: true }
            ]
        }
    },

    // obtener lista de obras
    created() {
        getAPI.get('/cajasChicas',)
            .then(response => {
                this.cajas = response.data
                console.log('datos de cajas recibidos')
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
        // obtener id de caja elegida
        onRowSelected(items) {
            if(this.isSelected == false) {
                this.isSelected = true
                this.$emit('items', items)
                this.$emit('row-selected', false)

            // deshabilitar botones si no hay una fila elegida
            }else {
                if(items['0'] != null){
                    this.$emit('items', items)
                }else{
                    this.isSelected = false
                    this.$emit('row-selected', true)
                }

                
            }
            
        },       
    },
}
</script>

<style lang="scss">
    @import '@/components/styles/table.scss'
</style>
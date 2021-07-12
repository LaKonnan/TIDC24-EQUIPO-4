<template>
  <div>
      <!-- tabla -->
      <b-table
        class = "table"
        selectable 
        :items="APIData" 
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
        props: ['gasto'],
        data () {
            return {
                APIData: [],
                perPage: 10,
                currentPage: 1,
                selectMode: 'single',
                selected: [],
                fields: [
                 {key: 'folio.S', label: 'Folio'},
                 {key: 'fechaEmision.S', label: 'Fecha Emisión'}, 
                 {key: 'horaEmision.S', label: 'Hora Emisión'}, 
                 {key: 'maquina.S', label: 'Máquina'}, 
                 {key: 'montoTotal.S', label: 'Monto Total'},
                 {key: 'nombreEstacion.S', label: 'Estación'}, 
                 {key: 'qtyBencina.S', label: 'Cantidad de Bencina (Lts)'}, 
                 {key: 'tipoComprobante.S', label: 'Tipo de Comprobante'}
                 ]
            }
        },
        
        created() {
            getAPI.get('/gastosCombustible',)
                .then(response => {
                    console.log('Obra API has received data')
                    this.APIData = response.data
                })
                .catch(err => {
                    console.log(err)
                })
        },
        
        computed: {
            rows() {
                return this.APIData.length
            }
        },

        methods: {
        onRowSelected(items) {
            this.selected = items
            this.$emit('row-selected', false);
            this.$emit('items', items);
        }
    }
}

</script>

<style>

</style>
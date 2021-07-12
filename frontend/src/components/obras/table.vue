<template>
  <div>
      <!-- tabla -->
      <b-table
        class = "table table-responsive-sm"
        id="table"
        ref="obras_table"
        :fields="fields"
        :items="obras" 
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
        aria-controls="table">
      </b-pagination>
  </div>
</template>

<script>
    import { getAPI } from '../axios-api'

    export default {
        props: ['obra'],
        data () {
            return {
                obras: [],
                perPage: 10,
                selectMode: 'single',
                currentPage: 1,
                selected: [],
                isSeleceted: false,

                // columnas con opcion a ordenar
                fields: [
                    { key: 'obraId.S', label: 'ID', sortable: true },
                    { key: 'encargado.S', label: 'Encargado', sortable: true }, 
                    { key: 'nombre.S', label: 'Nombre', sortable: true }, 
                    { key: 'estado.S', label: 'Estado', sortable: true }, 
                    { key: 'tipo.S', label: 'Tipo', sortable: true }
                ],
            }
        },
        
        computed: {
            // obtener cantidad de elementos de cajas para paginado
            rows() {
                return this.obras.length
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
            
            async get_obras() {
                const accessToken = await this.$auth.getTokenSilently()
                getAPI.get('/obras', {
                    headers: {
                        Authorization: `Bearer ${accessToken}`
                    }
                })
                .then(response => {
                    this.obras = response.data
                })
                .catch(err => {
                    console.log(err)
                })
            }
        },

        mounted() {
            // obtener lista de obras
            this.get_obras()
        },
    }

</script>

<style>

</style>
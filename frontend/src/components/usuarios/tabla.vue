<template>
    <div>
      <!-- tabla -->
      <b-table
        class = "table table-responsive-sm"
        id="table"
        :fields="fields"
        :items="usuarios" 
        :usuario="usuario"
        :select-mode="selectMode"
        :per-page="perPage"
        @row-selected="onRowSelected"
        :current-page="currentPage"
        hover
        selectable>
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
    props: ['usuario'],

    data () {
        return {
            fields: [
                { key: 'identities[0].user_id', label: 'Rut', sortable: true },
                { key: 'name', label: 'Nombre', sortable: true},
                { key: 'email', label: 'Email', sortable: true },
                { key: 'user_metadata.rol', label: 'Rol', sortable: true }
            ],
            usuarios: [],
            perPage: 10,
            selectMode: 'single',
            currentPage: 1,
            isSelected: false
        }
    },

    mounted() {
        this.get_users()
    },

    computed: {
        // obtener cantidad de elementos de usuarios para paginado
        rows() {
            return this.usuarios.length
        }
    },

    methods: {
        // obtener id de usuario seleccionada
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

        // obtener usuarios
        async get_users(){
            const accessToken = await this.$auth.getTokenSilently()
            console.log(accessToken)
            getAPI.get('/usuarios', {
                headers: {
                    Authorization: `Bearer ${accessToken}`
                }
            })
                    .then(response => {
                        console.log('Datos de usuario recibidos')
                        console.log(response.data)
                        this.usuarios = response.data
                    })
                    .catch(err => {
                        console.log(err)
                    })
        }
    }
}
</script>

<style lang="scss">
    @import '@/components/styles/table.scss'
</style>

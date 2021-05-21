<template>
    <div class="obras">
        <Navbar></Navbar>
        <div class="album py-5 bg-light">
          <div class="container">
              <h1>Obras de la empresa</h1>
                <div class="card" style="width: 50rem;">
                    <ul class="list-group list-group-flush">
                        <div class="row" v-for="obras in APIData" :key="obras.obraId">
                            <li class="list-group-item">
                                ID: {{obras.obraId.S}}
                                Residente: {{obras.encargado.S}}
                                Nombre: {{obras.nombre.S}}
                                Estado: {{obras.estado.S}}
                            </li>
                        </div>
                    </ul>
                </div>
          </div>
      </div>     
    </div>
</template>

<script>
    import { getAPI } from '../axios-api'
    import Navbar from '../components/Navbar'
    export default {
        name: 'Obras',
        data () {
            return {
                APIData: []
            }
        },
        components: {
            Navbar
        },
        created () {
            getAPI.get('/obras',)
                .then(response => {
                    console.log('Obra API has recieved data')
                    this.APIData = response.data
                })
                .catch(err => {
                    console.log(err)
                })
        }
    }
</script>

<style scoped>

</style>
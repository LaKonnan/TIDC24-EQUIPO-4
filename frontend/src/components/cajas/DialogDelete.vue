<template>
  <div>
    <b-modal id="modal-delete" size="xl" title="ELIMINAR CAJA CHICA" hide-footer>
        <b-card-text>
            <b-card>

            </b-card>
        </b-card-text>
        <center>
        <p><b>IMPORTANTE: </b>Una vez eliminada la caja chica esta no podrá ser recuperada, toda información sobre los gastos efectuados y fechas se perderán.</p>
        <p><b>Para confirmar la eliminación de la caja, por favor, ingresar su contraseña:</b></p></center>
        <b-form-input v-model="password" type="password" style="text-align: center;" @keyup="activateButton()"></b-form-input>
        <b-button class="normal-button" :disabled="button" @click="deleteCaja()" >ELIMINAR</b-button>
    </b-modal>
  </div>
</template>

<script>
import { getAPI } from '../axios-api'

export default {
    props: ['items'],
    data() {
        return {
            password: '',
            // recibir id de caja seleccionada
            data: [],
            button: true,
            caja: '',
            item_id: this.items[0].id_caja.S
        }
    },

    methods: {
        activateButton() {
            this.button = false
        },

        getData() {
            getAPI.get('/cajasChicas/' + this.caja,)
                .then(response => {
                    this.data = response.data
                })
        },

        deleteCaja() {
            const options = {
                headers: {
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Access-Control-Allow-Origin': '*'
                }
            }
            
            if(this.password == '123'){
                getAPI.delete('/cajaChica/'+ this.items[0].id_caja.S,'',options)
                    .then(res => {
                        console.log(res)
                    })
            }
        }
    },

    watch: {
        item_id: function(){
            this.caja = this.items[0].id_caja.S
            this.getData()
        }
    }
}
</script>

<style>

</style>
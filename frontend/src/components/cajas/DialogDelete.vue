<template>
  <div>
    <b-modal id="modal-delete" size="lg" title="ELIMINAR CAJA CHICA" hide-footer @before-open="getData()">
        <b-card-text>
            <b-card>
                <b-row>
                    <b-col>ID CAJA CHICA</b-col>
                    <b-col> {{ this.id_caja }} </b-col>
                </b-row>
                <b-row>
                    <b-col>OBRA</b-col>
                    <b-col> {{ this.id_obra }} </b-col>
                </b-row>
                <b-row>
                    <b-col>TIPO DE CAJA</b-col>
                    <b-col> {{ this.tipo }} </b-col>
                </b-row>
                <b-row>
                    <b-col>ESTADO</b-col>
                    <b-col> {{ this.estado }} </b-col>
                </b-row>
                <b-row>
                    <b-col>FECHA DE INICIO</b-col>
                    <b-col> {{ this.fecha_inicio }} </b-col>
                </b-row>
                <b-row>
                    <b-col>FECHA DE TÉRMINO</b-col>
                    <b-col> {{ this.fecha_termino }} </b-col>
                </b-row>
                <b-row>
                    <b-col>MONTO GASTOS</b-col>
                    <b-col> {{ this.monto_gastos }} </b-col>
                </b-row>
                <b-row>
                    <b-col>MONTO ASIGNADO</b-col>
                    <b-col> {{ this.monto_total }} </b-col>
                </b-row>
            </b-card>
        </b-card-text>
        <center>
        <p><b>IMPORTANTE: </b>Una vez eliminada la caja chica esta no podrá ser recuperada, toda información sobre los gastos efectuados y fechas se perderán. Tanto la caja chica como la caja de combustible serán eliminadas.</p>
        <p><b>Para confirmar la eliminación de la caja, por favor, ingresar su contraseña:</b></p></center>
        <b-form-input v-model="password" type="password" style="text-align: center;" @keyup="activateButton()"></b-form-input>
        <b-button class="normal-button" :disabled="button"  @click="deleteCaja()" >ELIMINAR</b-button>
    </b-modal>

    <!-- modal de exito -->
    <modal-success :message="succes_text" v-on:passData="sendMethod"/>

    <!-- modal de error -->
    <modal-error :message="error_text" v-on:passData="sendMethod"/>

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
            caja: [],
            button: true,
            
            // datos de caja
            id_caja: '',
            id_obra: 0,
            tipo: '',
            estado: '',
            fecha_inicio: '',
            fecha_termino: '',
            monto_gastos: '',
            monto_total: '',
            success_text: '',
            error_text: '' 
        }
    },

    methods: {
        activateButton() {
            this.button = false
        },

        getData() {
            getAPI.get('/cajasChicas/'+ this.items[0].id_caja.S ,)
                .then(response => {
                    this.caja = response.data
                    
                    // determinar datos
                    this.id_caja = this.caja[0].id_caja.S
                    this.id_obra = this.caja[0].id_obra.N
                    this.tipo = this.caja[0].tipo.S
                    this.estado = this.caja[0].estado.S
                    this.fecha_inicio = this.caja[0].fecha_inicio.S
                    this.fecha_termino = this.caja[0].fecha_termino.S
                    this.monto_gastos = this.caja[0].monto_gastos.S
                    this.monto_total = this.caja[0].monto_total.S
                })
        },

        deleteCaja() {
            const options = {
                headers: {
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Access-Control-Allow-Origin': '*'
                }
            }

            console.log(options)
            
            // obtener clave del usuario activo
        //     var pass =  $auth.user.password
        //     if(this.password == pass){
        //         getAPI.delete('/cajasChicas/'+ this.items[0].id_caja.S,'',options)
        //             .then(res => {
        //                 console.log(res)

        //                 console.log('creada')
        //                 this.success_text = 'Caja chica' + this.items[0].id_caja.S + 'eliminada con éxito'
                        
        //                 // resetear campos
        //                 this.resetForm()
                        
        //                 // recargar datos de tabla
        //                 this.$refs.cajas_table.refresh()

        //                 // mostrar modal de exito al crear
        //                 this.$bvModal.show('success_modal')
        //             })
        //     }else{
        //         this.error_text = 'Contraseña incorrecta, intente nuevamente'

        //         // mostrar modal de error
        //         this.$bvModal.show('error_modal')
        //     }
        },

        modalBack() {
            this.$bvModal.hide('error_modal')
            this.$bvModal.show('modal-delete')
        },

        // enviar métodos a componentes 
        sendMethod(data) {
            if (data.methodCall) return this[data.methodCall]();
        },

        // dejar variables vacías
        resetData() {
            this.id_caja = ''
            this.id_obra = ''
            this.tipo = ''
            this.estado = ''
            this.fecha_inicio = ''
            this.fecha_termino = ''
            this.monto_gastos = ''
            this.monto_total = ''
        }
    },

    mounted() {
        this.$root.$on('bv::modal::shown', (bvEvent, modalId) => {
            if( modalId == 'modal-delete') {
                this.getData()
                console.log('SE MOSTRARA EL MODAL DE DELETE', bvEvent, modalId)
            }
        })
    }
}
</script>

<style>

</style>
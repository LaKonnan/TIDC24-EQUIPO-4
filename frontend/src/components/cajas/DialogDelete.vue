<template>
  <div>
    <b-modal id="modal-delete" size="xl" title="ELIMINAR CAJA CHICA" hide-footer>
        <b-card-text>
            <b-card >
                <b-row>
                    <b-col>
                        ID
                    </b-col>

                    <b-col>
                        O556-01
                    </b-col>
                </b-row>

                <b-row>
                    <b-col>
                        Tipo de caja
                    </b-col>

                    <b-col>
                        Obra
                    </b-col>
                </b-row>

                <b-row>
                    <b-col>
                        Estado
                    </b-col>

                    <b-col>
                        Inactiva
                    </b-col>
                </b-row>

                <b-row>
                    <b-col>
                        Fecha de inicio
                    </b-col>

                    <b-col>
                        2021-05-15
                    </b-col>
                </b-row>

                <b-row>
                    <b-col>
                        Fecha de término
                    </b-col>

                    <b-col>
                        2021-06-15
                    </b-col>
                </b-row>

                <b-row>
                    <b-col>
                        Monto de gastos
                    </b-col>

                    <b-col>
                        145600
                    </b-col>
                </b-row>

                <b-row>
                    <b-col>
                        Monto total
                    </b-col>

                    <b-col>
                        180000
                    </b-col>
                </b-row>
            </b-card>
        </b-card-text>
        <center>
        <p><b>IMPORTANTE: </b>Una vez eliminada la caja chica esta no podrá ser recuperada, toda información sobre los gastos efectuados y fechas se perderán.</p>
        <p><b>Para confirmar la eliminación de la caja, por favor, ingresar su contraseña:</b></p></center>
        <b-form-input v-model="password" type="password" style="text-align: center;"></b-form-input>
        <b-button class="normal-button">ELIMINAR</b-button>
    </b-modal>
  </div>
</template>

<script>
export default {
    data() {
        return {
            password: ''
        }
    }
}
</script>

<style>

</style>
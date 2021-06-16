<template>
  <div>
    <b-modal id="modal-view" size="xl" title="CAJA CHICA" hide-footer>
        <b-card-text>
            <b-card>
                <b-row>
                    <b-col>
                        ID
                    </b-col>

                    <b-col>
                        {{ this.items[0].id_caja.S }}
                    </b-col>
                </b-row>

                <b-row>
                    <b-col>
                        Tipo de caja
                    </b-col>

                    <b-col>
                        {{ this.items[0].tipo.S }}
                    </b-col>
                </b-row>

                <b-row>
                    <b-col>
                        Estado
                    </b-col>

                    <b-col>
                        {{ this.items[0].estado.S }}
                    </b-col>
                </b-row>

                <!-- <b-row>
                    <b-col>
                        Fecha de inicio
                    </b-col>

                    <b-col>
                        {{ this.items[0].fecha_incio.S }}
                    </b-col>
                </b-row>

                <b-row>
                    <b-col>
                        Fecha de término
                    </b-col>

                    <b-col>
                        {{ this.items[0].fecha_termino.S }}
                    </b-col>
                </b-row> -->

                <b-row>
                    <b-col>
                        Monto de gastos
                    </b-col>

                    <b-col>
                        {{ this.items[0].monto_gastos.S }}
                    </b-col>
                </b-row>

                <b-row>
                    <b-col>
                        Monto total
                    </b-col>

                    <b-col>
                        {{ this.items[0].monto_total.S }}
                    </b-col>
                </b-row>
            </b-card>
        </b-card-text>
    </b-modal>
  </div>
</template>

<script>
export default {
    props: ['items']

}
</script>

<style>

</style>
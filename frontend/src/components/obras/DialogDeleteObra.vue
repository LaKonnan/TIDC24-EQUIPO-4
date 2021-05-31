<template>
    <div>
        <b-modal id="modal-xld" size="xl" title="ELIMINAR OBRA" hide-footer>
            <b-tabs pills card vertical v-model="tabIndex">
                <!-- Modal que debe contener los datos (en readonly) para eliminar -->
                
                    <b-card-text>
                        Los siguientes datos de obra seleccionada serán eliminados
                        <br><br>
                        Nombre de la obra
                        <b-form-input v-model="selectedObra"></b-form-input>

                        Encargado de la obra
                        <b-form-input v-model="selectedEncargado"></b-form-input>

                        Estado de la obra
                        <b-form-input v-model="selectedState"></b-form-input>

                        <b-button :disabled="btnStep1" id="btnStep1" class="button-next dark-button" @click="next1()">Eliminar</b-button>
                        <b-button :disabled="btnExit1" id="btnExit1" class="button-next dark-button" >Salir</b-button>
                    </b-card-text>
             </b-tabs>
        </b-modal>
    </div>
</template>

<script>
export default {
    data () {
        return  {
            tabIndex: 2,
            step: 1,
            btnStep1: true,
            selectedObra: null,
            selectedEncargado: null,
            selectedState: null,
        }
    },
    methods: {
    updated() {
        this.nextStep()
        console.log(this.tabIndex)
    }    
  }
}
</script>

<style> </style> 
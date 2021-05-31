<template>
    <div>
        <b-modal id="modal-xle" size="xl" title="EDITAR OBRA" hide-footer>
            <b-tabs pills card vertical v-model="tabIndex">
                <!-- Modal que debe permitir editar datos seleccionados de la tabla -->
                
                    <b-card-text>
                        Los siguientes datos de obra seleccionada serán editados
                        <br><br>
                        Nombre de la obra
                        <b-form-input v-model="editObra" ></b-form-input>

                        Encargado de la obra
                        <b-form-input v-model="editEncargado" ></b-form-input>

                        Estado de la obra
                        <b-form-select v-model="editState"></b-form-select>

                        <b-button :disabled="btnStep1" id="btnStep1" class="button-next dark-button" @click="next1()">Editar</b-button>
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
            editObra: null,
            editEncargado: null,
            editState: null,
           
            options3: [
                { value: 'Activa', text: 'Activa'},
                { value: 'Inactiva', text: 'Inactiva'}
                
            ]
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
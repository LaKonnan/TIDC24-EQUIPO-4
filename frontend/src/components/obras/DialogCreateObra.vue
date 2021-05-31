<template>
    <div>
        <b-modal id="modal-xlc" size="xl" title="NUEVA OBRA" hide-footer>
            <b-tabs pills card vertical v-model="tabIndex">
                <!-- Modal que debe permitir crear una obra -->
                
                    <b-card-text>
                        Nombre de la obra
                        <b-form-input  v-model="nombreObra"></b-form-input>

                        Encargado de la obra
                        <b-form-input v-model="encargadoObra" ></b-form-input>

                        Estado de la obra
                        <b-form-select v-model="estadoObra" :options="options3"></b-form-select>

                        <b-button :disabled="btnStep1" id="btnStep1" class="button-next dark-button" @click="next1()">Crear Obra</b-button>
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
            nombreObra: null,
            encargadoObra: null,
            estadoObra: null,
           
            options3: [
                { value: 'Activa', text: 'Activa'},
                { value: 'Inactiva', text: 'Inactiva'}
                
            ]
        }
    },

    methods: {
        nextStep() {
            switch(this.step){
                case 1 :
                    if(this.nombreObra != null && this.encargadoObra != null) {
                        this.step2 = false
                    }
                    if( this.nombreObra != null && this.encargadoObra != null && this.estadoObra != null){
                        this.btnStep1 = false
                        this.step = 2
                    }
                    break
                case 2:
                    
                    break
                case 3:
                    break
                default:
                    break
            }
            
        },
        next1() {
            this.step2 = false
            const next = document.getElementById('Step1')
            next.classList.remove('active')
            const step = document.getElementById('Step2')
            step.classList.add('active')
            this.tabIndex++
            console.log(this.tabIndex)
        }
    },
    
    updated() {
        this.nextStep()
        console.log(this.tabIndex)
    }    
}
</script>

<style> </style> 
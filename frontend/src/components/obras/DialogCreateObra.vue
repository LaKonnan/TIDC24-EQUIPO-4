<template>
    <div>
      <b-modal ref="create" id="modal-xlc" size="xl" title="NUEVA OBRA" hide-footer>
          <b-tabs pills card vertical v-model="tabIndex">
            <!-- paso 1 -->
            <b-tab title="PASO 1" active id="step1">
                    <b-card-text>
                        ID
                        <b-form-input  v-model="obraid" @keyup="activateButton()" type="number" :state="validLength" aria-describedby="input-live-feedback1" ></b-form-input>
                        <b-form-invalid-feedback id="input-live-feedback1">
                        Requiere ingresar el ID de la obra
                        </b-form-invalid-feedback>
                        Encargado de la obra
                        <b-form-input  v-model="encargado" @keyup="activateButton()" :state="validLength2" aria-describedby="input-live-feedback1" ></b-form-input>
                        <b-form-invalid-feedback id="input-live-feedback1">
                        Requiere ingresar un encargado
                    </b-form-invalid-feedback>
                        Nombre de la obra
                        <b-form-input v-model="nombre" @keyup="activateButton()" :state="validLength3" aria-describedby="input-live-feedback2" ></b-form-input>
                        <b-form-invalid-feedback id="input-live-feedback2">
                        Requiere ingresar el nombre de la obra
                    </b-form-invalid-feedback>
                    
                        Estado de la obra
                        <b-form-select v-model="estado" :options="options1" @change="activateButton()" ></b-form-select>

                         Tipo
                        <b-form-select v-model="tipo" :options="options2" @change="activateButton()"></b-form-select>

                        <b-button :disabled="btnStep1" id="btnStep1" class="button-next dark-button" @click="next1()">Siguiente</b-button>
                    </b-card-text>
            </b-tab>

            <!-- paso  2 -->
            <b-tab title="PASO 2" id="step2" :disabled="step2">
               <b-card-text>
                        <!-- resumen de nueva obra -->
                <b-card  title="RESUMEN DE NUEVA OBRA">
                   <b-card-text>
                      <b-row>
                        <b-col>ID</b-col>
                        <b-col>{{ this.obraid }}</b-col>
                   </b-row>
                   <b-row>
                        <b-col>Encargado de la obra</b-col>
                        <b-col>{{ this.encargado }}</b-col>
                   </b-row>

                   <b-row>
                        <b-col>Nombre de la obra</b-col>
                        <b-col>{{ this.nombre }}</b-col>
                   </b-row>

                   <b-row>
                        <b-col>Estado de la obra</b-col>
                        <b-col>{{ this.estado }}</b-col>
                   </b-row>

                   <b-row>
                        <b-col>Tipo</b-col>
                        <b-col>{{ this.tipo }}</b-col>
                   </b-row>
                   </b-card-text>
               </b-card>
               <br>
                        <p>Una vez presionado el botón, se registrará la obra en el sistema.</p>
                    <b-button id="btnStep3" class="button-next dark-button" @click="create()">GUARDAR</b-button>
             </b-card-text>
            </b-tab>
        </b-tabs>
      </b-modal>
      <b-modal ref="success-modal" id="modal-no-backdrop" hide-backdrop hide-footer hide-header>
            <center>
                <p class="success"><b-icon icon="check-circle" animation="fade"></b-icon></p>
                <p>Obra creada con éxito</p>
            </center>
    </b-modal>
  </div>
</template>

<script>
import { getAPI } from '../axios-api';



export default {
   
  data() {
    return {
      obraid:'',
      encargado: '',
      nombre: '',
      success: false,
      tabIndex: 2,
      btnStep1: true,
      step2: true,
      estado: null,
      tipo: null,
      options1: [
                { value: 'Activa', text: 'Activa'},
                { value: 'Inactiva', text: 'Inactiva'},
                { value: 'Finalizada', text: 'Finalizada' }
            ],
      options2: [
                { value: 'Obra', text: 'Obra'},
                { value: 'Gerencia', text: 'Gerencia'},
                { value: 'Oficina', text: 'Oficina central'}
            ],
      
    };
  },
  
  methods: {
   
   activateButton(){
     switch(this.tabIndex){
     case 0:
      if(![this.obraid, this.encargado, this.nombre, this.estado, this.tipo].includes(null)) {
        this.btnStep1 = false
        this.step2 = false
     }
     break;

     case 1:
       break;
     }
     
   },

   // pasar a paso 2 a traves del boton de paso 1
        next1() {
            const next = document.getElementById('step1')
            next.classList.remove('active')
            const step = document.getElementById('step2')
            step.classList.add('active')
            this.tabIndex++
        },


     create(){
     console.log(this.obraid)
     const options = {
       headers: {
         'Content-Type': 'application/json;charset=UTF-8',
         'Access-Control-Allow-Origin': '*'
       }
     }

     const data = JSON.stringify(
       {
         obraId: this.obraid,
         encargado: this.encargado,
         estado: this.estado,
         nombre: this.nombre,
         tipo: this.tipo
       }
     )

     getAPI.post('/obras', data, options)
        .then((res) =>{
          if(res.statusText == 'OK'){
            this.success = true
            this.$refs['create'].hide()
            setTimeout(() => {
               this.$refs['success-modal'].show()
            },500)
            this.$refs['success-modal'].hide()
          }

        })
        .catch((err)=>{
          console.log('Error: ', err)
        })

     }
  },

   computed: {
      validLength() {
        return this.obraid.length > 0 ? true : false
      },
      validLength2() {
        return this.encargado.length > 0 ? true : false
      },
       validLength3() {
        return this.nombre.length > 0 ? true : false
      },
    },
    

  }

</script>


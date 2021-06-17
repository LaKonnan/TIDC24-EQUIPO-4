<template>
    <div>
        <b-modal ref="create" id="modal-xle" size="xl" title="EDITAR OBRA" hide-footer>    
                <b-card-text>
                        Los siguientes datos de obra seleccionada serán editados
                        <hr>
                        <b>Obra:</b>
                          <b-card-text>
                      <b-row>
                        <b-col>ID</b-col>
                        <b-col>{{items[0].obraId.S}}
                          {{setobraID(items[0].obraId.S)}}</b-col>
                   </b-row>
                   <b-row>
                        <b-col>Encargado de la obra</b-col>
                        <b-col>{{items[0].encargado.S}}</b-col>
                   </b-row>

                   <b-row>
                        <b-col>Nombre de la obra</b-col>
                        <b-col>{{items[0].nombre.S}}</b-col>
                   </b-row>

                   <b-row>
                        <b-col>Estado de la obra</b-col>
                        <b-col>{{items[0].estado.S}}</b-col>
                   </b-row>

                   <b-row>
                        <b-col>Tipo</b-col>
                        <b-col>{{items[0].tipo.S}}</b-col>
                   </b-row>
                   </b-card-text>
                  
                  <hr>
                    

                    Encargado de la obra
                    <b-form-input v-model="encargado" value=""  @keyup="activateButton()" :state="validLength2" aria-describedby="input-live-feedback2"></b-form-input>
                    <b-form-invalid-feedback id="input-live-feedback2">
                        Requiere ingresar un encargado de la obra
                    </b-form-invalid-feedback>

                    Nombre de la obra
                    <b-form-input v-model="nombre" value=""  @keyup="activateButton()" :state="validLength3" aria-describedby="input-live-feedback3"></b-form-input>
                    <b-form-invalid-feedback id="input-live-feedback3">
                        Requiere ingresar el nombre de la obra
                    </b-form-invalid-feedback>

                   Estado de la obra
                    <b-form-select v-model="estado" :options="options1" @change="activateButton()" ></b-form-select>

                   Tipo
                    <b-form-select v-model="tipo" :options="options2" @change="activateButton()"></b-form-select>
                <b-button :disabled="btnEdit" id="btnEdit" class="button-next dark-button" @click="createEdit()">Editar</b-button>
                        
          </b-card-text>
        </b-modal>
        <b-modal ref="success-modal" id="modal-no-backdrop" hide-backdrop hide-footer hide-header>
          <center>
          <p class="success"><b-icon icon="check-circle" animation="fade"></b-icon></p>
          <p>Obra editada con éxito</p>
          </center>
    </b-modal>
    </div>
</template>

<script>
import { getAPI } from '../axios-api';


export default {
  
  props: ['items'],
  data() {
    return {
      obraid:'',
      encargado: '',
      nombre: '',
      btnEdit: true,
      estado: null,
      tipo: null,
        options1: [
                { value: 'Activa', text: 'Activa'},
                { value: 'Inactiva', text: 'Inactiva'},
                { value: 'Finalizada', text: 'Finalizada'}
            ],
            options2: [
                { value: 'Obra', text: 'Obra'},
                { value: 'Gerencia', text: 'Gerencia'},
                { value: 'Oficina', text: 'Oficina central'}
            ],
      
    };
  },
  methods: {
    setobraID(obraId){
      this.obraid = obraId;
    },
   activateButton(){
      if(![this.encargado, this.nombre, this.estado, this.tipo].includes(null)) {
        this.btnEdit = false
        }
     },
    
   createEdit(){
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
    
    getAPI.put('/obras', data, options)
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
      validLength2() {
        return this.encargado.length > 0 ? true : false
      },
       validLength3() {
        return this.nombre.length > 0 ? true : false
      }
    },
  
}
    
    

    
  

</script>


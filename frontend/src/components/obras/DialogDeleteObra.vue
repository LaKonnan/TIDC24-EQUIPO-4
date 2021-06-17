<template>
    <div>
        <b-modal id="modal-xld" size="xl" title="ELIMINAR OBRA" hide-footer>    
                <b-card-text>
                        Los siguientes datos de obra seleccionada serán eliminados
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
                    <p><b>IMPORTANTE: </b>Una vez eliminada la obra, no podrá ser recuperada.</p>
                    <b-form-input v-model="password" type="password" style="text-align: center;" @keyup="activateButton()"></b-form-input>
                    
                <b-button  class="button-next dark-button" disabled:button @click="deleteObra()">Eliminar Obra</b-button>
                        
          </b-card-text>
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
      password:''
     
    };
  },
 
  methods: {
    setobraID(obraId){
      this.obraid = obraId;
    },
    activateButton() {
            this.button = false
        },

    deleteObra(){
      console.log(this.obraid)
      const options = {
        headers: {
         'Content-Type': 'application/json;charset=UTF-8',
         'Access-Control-Allow-Origin': '*'
        }
      }

     if(this.password == '123'){
       getAPI.delete('/obras/'+this.items[0].obraId.S,'',options)
        .then((res) =>{
          console.log('Datos Eliminados: ', res)
        })
      }
    }
  }
}  
  

</script>
 
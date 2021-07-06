<template>
    <div>
        <b-modal id="modal-xlu" size="xl" title="Subir Nuevo Reglamento" hide-footer @hidden="onHidden">
            <b-col>
                <b-row>{{file.name}}</b-row>
            </b-col>
            <br><br>
            <center>
            <p><b>IMPORTANTE: </b>Una vez actualizado el documento no podrá recuperar el antiguo</p>
            <p><b>¿Desea subir un nuevo reglamento?</b></p></center>
            <b-button class="dark-button" @click="onClickConfirmar">Confirmar</b-button>
            <b-button class="dark-button" @click="onClickCancelar">Cancelar</b-button>
        </b-modal>
    </div>
</template>

<script>
//import { getAPI } from '../axios-api';

export default {
  props: ['file'],
  data() {

  },
  methods: {
    onHidden() {
      console.log('modal cerrado')
      //actualizar vista del pdf
    },
    onClickConfirmar() {
        console.log('boton subir archivo')
        this.$root.$emit('bv::hide::modal','modal-xlu')
    },
    onClickCancelar() {
        console.log('boton cancelar')
        this.$root.$emit('bv::hide::modal','modal-xlu')
    }
  }
};
</script>
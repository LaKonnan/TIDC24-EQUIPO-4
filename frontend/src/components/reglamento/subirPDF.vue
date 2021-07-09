<template>
  <div>
    <b-card class="card">
      <b>El nombre del archivo debe ser "reglamento" y debe estar en formato pdf</b>
      <b-form-file
        v-model="file"
        :state="Boolean(file)"
        placeholder="Puede arrastrar y soltar el archivo aquí..."
        drop-placeholder="Suelte el archivo aquí..." 
      ></b-form-file>

      <div class="mt-3">Archivo seleccionado: {{ file ? file.name : '' }}</div>

      <b-button v-b-modal.modal-xlu>Subir Archivo</b-button>

      <dialog-upload :file=file />
      </b-card>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        file: null
      }
    },
    components: {
      'dialog-upload': require('@/components/reglamento/DialogUpload.vue').default
    }
  }
</script>

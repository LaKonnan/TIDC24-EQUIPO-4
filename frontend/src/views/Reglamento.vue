<template>
  <div class="content">
    <b-button @click="forceRerender" >Actualizar</b-button>
    <reglamentoPDF :key="componentKey" />
    <subirPDF :componentKey=componentKey />
  </div>
</template>

<script>
  export default {
    data(){
      return {
        componentKey: 0
      }
    },
    components: {
            'reglamentoPDF': require('../components/reglamento/reglamentoPDF.vue').default,
            'subirPDF': require('../components/reglamento/subirPDF.vue').default
    },
    created() {
      this.$root.$refs.A = this
    },
    methods: {
      forceRerender() {
        this.componentKey += 1;
      }
    }
  }
</script>
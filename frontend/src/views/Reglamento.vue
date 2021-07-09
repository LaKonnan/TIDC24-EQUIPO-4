<template>
  <div class="content">
    <b-card class="card">
      <b-button class="float-right" @click="forceRerender" >
        <b-icon icon="arrow-clockwise"></b-icon>
      </b-button>
      <reglamentoPDF :key="componentKey" />
    </b-card>
    <hr>
    <subirPDF :componentKey=componentKey />
    <hr>
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
    methods: {
      forceRerender() {
        this.componentKey += 1;
      }
    }
  }
</script>

<style>
.content {
  margin-top: 40px;
}

</style>
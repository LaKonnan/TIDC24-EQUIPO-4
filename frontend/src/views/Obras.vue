<template>
    <div class="obras content">
        <br>
        <!-- titulo -->
        <p class="dark-title">GESTIÓN DE OBRAS</p>
        <hr class="hr">
        <!--Tabla que recibe datos de obras y las muestra -->
        <table-obras/>

        <!-- botones para crud -->
        <buttons />
  </div>     
    
    
</template>

<script>
    export default {
        name: 'Obras',
        components: {
            'table-obras': require('../components/obras/table.vue').default,
            'buttons': require('../components/obras/buttons').default
        }
    }
    
</script>

<style lang="scss">
    @import '../components/estilos.scss';

</style>
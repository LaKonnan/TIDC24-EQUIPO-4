<template>
    <div class="content">
        <!--tabla  -->
        <table-obras 
            @row-selected="onRowSelected" 
            @items="rowItems"/>

        <!-- botones -->
        <buttons :selectedRow="selectedRow" :items="items" />
  </div>     

</template>

<script>
    export default {
        name: 'Obras',
        data(){
            return{
                selectedRow: true,
                items: []
            }
        },

        components: {
            'table-obras': require('../components/obras/table').default,
            'buttons': require('../components/obras/buttons').default,
        },

        methods: {
            // fila seleccionada
            onRowSelected(params) {
                this.selectedRow = params
            },

            // datos de fila
            rowItems(params){
                this.items = params;
            }
        }
    }
    
</script>

<style lang="scss">
  @import '@/components/styles/global.scss';
</style>
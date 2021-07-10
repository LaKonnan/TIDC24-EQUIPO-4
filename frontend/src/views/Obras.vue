<template>
    <div class="content">
        <!-- resumen -->  
        
        <!--tabla  -->
        <table-obras @row-selected="onRowSelected" @items="rowItems"/>

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
            'table-obras': require('../components/obras/table.vue').default,
            'buttons': require('../components/obras/buttons').default
        },
        methods: {
            onRowSelected(params) {
                this.selectedRow = params
            },
            rowItems(params){
                this.items = params;
            }
        }
    }
    
</script>

<style>
</style>
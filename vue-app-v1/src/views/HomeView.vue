<template>
    <layout-default>
        <v-sheet
            min-height="70vh"
            rounded="lg"
        >
            <v-progress-circular
                v-if="liste == null"
                color="teal-lighten-3"
                indeterminate
                :size="128"
                :width="5"
            ></v-progress-circular>
            <TableData
                v-else
                :listPharmacy="liste"
                tableHeight="70vh"
                clickCell="clickCellHome"
                :displayInfosMedocs=true
            />
        </v-sheet>
    </layout-default>
</template>

<script>
    import TableData from '@/components/TableData.vue';
    export default {
        components: { TableData },
        data() {
            return {
                liste: null
            }
        },
        async created() {
            const response = (await this.$axios.get('/client/list-pharmacy')).data;
            this.liste = response
            //console.log(response)
        },
    }
</script>

<style>
</style>
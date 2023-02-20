<template>
    <layout-default>
        <v-sheet
            min-height="70vh"
            rounded="lg"
        >
            <TableData
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
                listMedocs: [
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                ],
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
<template>
    <layout-default>
        <v-sheet
            min-height="70vh"
            rounded="lg"
        >
            <v-progress-circular
                v-if="liste.length === 0"
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
                liste: []
            }
        },
        async created() {
            //const response = (await this.$axios.get('/client/list-pharmacy')).data;
            const res = (await this.$axios.get(`/client/medocs`)).data.data;
            res.filter( async obj => {
                let { idMol, catMedoc, nameMedoc } = obj;
                let nameMol = await this.$store.dispatch('getMoleculeById', {axios: this.$axios, idMol});
                this.liste.push({ nameMol, catMedoc, nameMedoc});
            });
        },
    }
</script>

<style>
</style>
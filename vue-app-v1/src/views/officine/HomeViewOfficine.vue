<template>
    <AppBarOfficine />
    <v-container class="grid w-100 h-100" fluid>
        <LeadSearchBar class="child1" />
        <v-sheet min-height="80vh" rounded="lg" class="child2 pa-16" elevation="5">
            <v-row>
                <v-col>
                    <v-btn class="w-100 h-100 text-h6" rounded="lg" color="teal-lighten-3">GESTION DU STOCK DE L'OFFICINE</v-btn>
                </v-col>
                <v-col>
                    <v-btn class="w-100 h-100 text-h6 btn" rounded="lg" color="teal-lighten-3">SAISIE DE MÉDICAMENTS</v-btn>
                </v-col>
                <v-col>
                    <v-btn class="w-100 h-100 text-h6 btn" rounded="lg" color="teal-lighten-3">TRAITEMENT DES ORDONNANCES</v-btn>
                </v-col>
            </v-row>

            <v-row>
                <v-col>
                    <v-btn class="w-100 h-100 text-h6 btn" rounded="lg" color="teal-lighten-3">HISTORIQUE</v-btn>
                </v-col>
                <v-col>
                    <v-btn class="w-100 h-100 text-h6 btn" rounded="lg" color="teal-lighten-3">STATISTIQUES DE VENTE</v-btn>
                </v-col>
                <v-col>
                    <v-btn class="w-100 h-100 text-h6 btn" rounded="lg" color="teal-lighten-3">PARAMÈTRES</v-btn>
                </v-col>
            </v-row>
        </v-sheet>
    </v-container>
    
</template>

<script>
    import LeadSearchBar from '@/components/LeadSearchBar.vue';
    import AppBarOfficine from '@/components/AppBarOfficine.vue';
    export default {
        name: "HomeViewOfficine",
        components: { LeadSearchBar, AppBarOfficine }
    }
</script>

<style scoped>
    .grid {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        grid-row-gap: 10px;
        background-color: #eeeeeeff;
    }

    .child1 {
        grid-column: 2 / span 4;
    }

    .child2 {
        grid-column: 2 / span 4;
        grid-row: 2;
        display: grid;
    }

    .bg-teal-lighten-3 {
        color: #fff !important;
    }
</style>
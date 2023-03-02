<template>
    <LayoutOfficine>
        <v-sheet min-height="70vh" rounded="lg" class="pa-16" elevation="5">
            <h1 class="leadTitle">gestion du stock de l'officine</h1>
            <v-sheet min-height="50vh" class="grid mt-16">
                <v-col>
                    <v-btn class="w-100 h-50 text-h6" rounded="lg" color="teal-lighten-3">
                        ORDONNANCES REÇUES
                    </v-btn>
                </v-col>
                <v-col>
                    <v-btn class="w-100 h-50 text-h6" rounded="lg" color="teal-lighten-3">
                        ENREGISTRER ORDONNANCE
                    </v-btn>
                </v-col>
                <v-col>
                    <v-btn class="w-100 h-50 text-h6" rounded="lg" color="teal-lighten-3">
                        HISTORIQUE ORDONNANCES TRAITÉES
                    </v-btn>
                </v-col>
            </v-sheet>
        </v-sheet>
    </LayoutOfficine>
</template>

<script>
    export default {
        name: "HandlePrescip",
    }
</script>

<style scoped>
    .leadTitle {
        text-transform: uppercase;
        text-align: center;
    }

    .grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
    }
</style>
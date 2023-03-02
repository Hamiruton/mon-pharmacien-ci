<template>
    <LayoutOfficine>
        <v-sheet min-height="70vh" rounded="lg" class="pa-16" elevation="5">
            <h1 class="leadTitle">gestion du stock de l'officine</h1>
            <v-sheet min-height="50vh" class="grid">
                <v-col v-for="cat, index in categoryDrug" :key="index">
                    <v-btn class="w-100 h-100 text-h6" rounded="lg" color="teal-lighten-3">
                        <span class="cat-btn">{{ cat }}</span>
                    </v-btn>
                </v-col>
            </v-sheet>
        </v-sheet>
    </LayoutOfficine>
</template>

<script>
    export default {
        name: "HandleStock",
        data() {
            return {
                categoryDrug: [
                    "antipaludique",
                    "grippe",
                    "antibiotique",
                    "antifongique",
                    "duriétique",
                    "antiarythmiques",
                    "antiémétiques",
                    "antigènes",
                    "micro-immunothérapie"
                ]
            }
        },
        
    }
</script>

<style scoped>
    .leadTitle {
        text-transform: uppercase;
        text-align: center;
    }

    .grid {
        display: grid;
        /*overflow-y: scroll;*/
        grid-template-columns: repeat(3, 1fr);
    }

    .cat-btn {
        text-transform: uppercase;
        font-weight: bold;
    }
</style>
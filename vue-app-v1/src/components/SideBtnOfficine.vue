<template>
    <v-row>
        <v-col cols="12">
            <v-btn
                :to="{ name: 'homeOfficine' }"
                color="teal-lighten-3"
                size="x-large"
                rounded="lg"
                title="Cliquer pour retourner au menu"
                class="w-100"
            >ACCUEIL</v-btn>
        </v-col>
        <v-col cols="12" v-show="$route.name !== 'register_drugs'">
            <v-btn
                :to="{ name: 'register_drugs' }"
                color="teal-lighten-3"
                size="x-large"
                rounded="lg"
                title="Cliquer pour retourner au menu"
                class="w-100"
            >ENTRÉE MÉDICAMENT</v-btn>
        </v-col>
        <v-col cols="12" v-show="$route.name !== 'HandlePrescrip'">
            <v-btn
                :to="{ name: 'HandlePrescrip' }"
                color="teal-lighten-3"
                size="x-large"
                rounded="lg"
                title="Cliquer pour retourner au menu"
                class="w-100"
            >TRAITEMENT ORDONNANCE</v-btn>
        </v-col>
        <v-col cols="12" v-show="$route.name !== 'stats'">
            <v-btn
                :to="{ name: 'stats' }"
                color="teal-lighten-3"
                size="x-large"
                rounded="lg"
                title="Cliquer pour retourner au menu"
                class="w-100"
            >STATISTIQUES</v-btn>
        </v-col>
        <v-col cols="12" v-show="$route.name !== 'HandleStock'">
            <v-btn
                :to="{ name: 'HandleStock' }"
                color="teal-lighten-3"
                size="x-large"
                rounded="lg"
                title="Cliquer pour voir l'historique de tes activités"
                class="w-100"
            >GESTION STOCK</v-btn>
        </v-col>
        <v-col cols="12" v-show="$route.name !== 'historic'">
            <v-btn
                :to="{ name: 'historic' }"
                color="teal-lighten-3"
                size="x-large"
                rounded="lg"
                title="Cliquer pour voir les paramètres"
                class="w-100"
            >HISTORIQUE</v-btn>
        </v-col>
        <v-col cols="12">
            <v-btn
                color="teal-lighten-3"
                size="x-large"
                rounded="lg"
                title="Cliquer pour voir about"
                class="w-100"
            >PARAMÈTRES</v-btn>
        </v-col>
    </v-row>
</template>

<script>
    export default {
        name: "SideBtnOfficine"
    }
</script>
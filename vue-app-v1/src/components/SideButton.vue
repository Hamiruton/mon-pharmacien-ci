<template>
    <v-row>
        <v-col>
            <v-btn
                :to="{ name: 'home' }"
                color="teal-lighten-3"
                size="x-large"
                rounded="lg"
                title="Cliquer pour retourner au menu"
                class="w-100"
            >HOME</v-btn>
        </v-col>
        <v-col>
            <Prescription />
        </v-col>
        <v-col>
            <v-btn
                color="teal-lighten-3"
                size="x-large"
                rounded="lg"
                title="Cliquer pour voir les pharmacies (de garde)"
                class="w-100"
            >PHARMACIE</v-btn>
        </v-col>
        <v-col>
            <v-btn
                color="teal-lighten-3"
                size="x-large"
                rounded="lg"
                title="Cliquer pour voir l'historique de tes activités"
                class="w-100"
            >HISTORIQUE</v-btn>
        </v-col>
        <v-col>
            <v-btn
                :to="{ name: 'settings' }"
                color="teal-lighten-3"
                size="x-large"
                rounded="lg"
                title="Cliquer pour voir les paramètres"
                class="w-100"
            >PARAMÈTRES</v-btn>
        </v-col>
        <v-col>
            <v-btn
                :to="{ name: 'about' }"
                color="teal-lighten-3"
                size="x-large"
                rounded="lg"
                title="Cliquer pour voir about"
                class="w-100"
            >A PROPOS DE NOUS</v-btn>
        </v-col>
    </v-row>
</template>

<script setup>
import Prescription from './Prescription.vue';

</script>
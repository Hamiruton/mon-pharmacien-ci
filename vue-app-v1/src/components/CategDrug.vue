<template>
    <v-btn class="w-100 h-100 text-h6" rounded="lg" color="teal-lighten-3" @click="toggleDialog">
        <span class="cat-btn">{{ categ }}</span>
    </v-btn>
    <v-dialog
        v-model="dialog"
        fullscreen
        :scrim="true"
        transition="dialog-bottom-transition">
        <v-sheet>
            <v-toolbar color="teal-darken-4">
                <v-btn
                    icon
                    dark
                    @click="toggleDialog">
                    <v-icon>mdi-close</v-icon>
                </v-btn>
                <v-toolbar-title>Catégorie Médicaments {{ categ }}</v-toolbar-title>
                <v-spacer></v-spacer>
            </v-toolbar>
            <v-container class="grid w-100" fluid>
                <v-sheet class="child2 py-16" max-height="80vh" rounded="lg" elevation="5">
                    <DisplayInList v-for="drug, index in drugInCateg" :key="index" :content="drug.nameMedoc">
                        <template #actions>
                            <SeeMoreDrugBtn :drug="drug" />
                            <DeleteDrugBtn :drug="drug.nameMedoc" />
                        </template>
                    </DisplayInList>
                </v-sheet>
            </v-container>
        </v-sheet>
    </v-dialog>
</template>

<script>
    import DisplayInList from './DisplayInList.vue';
    import DeleteDrugBtn from './DeleteDrugBtn.vue';
    import SeeMoreDrugBtn from './SeeMoreDrugBtn.vue';
    export default {
        name: "CategDrug",
        props: ['categ'],
        components: {
            DisplayInList,
            DeleteDrugBtn,
            SeeMoreDrugBtn
        },
        data() {
            return {
                dialog: false,
                drugInCateg: [],
            }
        },
        methods: {
            toggleDialog() {
                this.dialog = !this.dialog;
            },
        },
        async created() {
            const idOfficine = this.$store.getters.idUser;
            const response = (await this.$axios.get(`/officine/stock/${idOfficine}/${this.categ}`)).data.data;
            this.drugInCateg = response;
        }
    }
</script>

<style scoped>
    .cat-btn {
        text-transform: uppercase;
        font-weight: bold;
    }

    .grid {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        height: calc(100% - 64px);
        background-color: #eeeeeeff;
    }

    .child2 {
        grid-column: 2 / span 4;
    }
</style>
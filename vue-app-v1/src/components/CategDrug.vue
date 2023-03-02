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
                    <DisplayInList content="Paracetamol">
                        <template #actions>
                            <v-btn icon="mdi-eye" color="teal-lighten-3" variant="elevated"></v-btn>
                            <v-btn icon="mdi-delete" color="error" variant="elevated"></v-btn>
                        </template>
                    </DisplayInList>
                </v-sheet>
            </v-container>
        </v-sheet>
    </v-dialog>
</template>

<script>
    import DisplayInList from './DisplayInList.vue';
    export default {
        name: "CategDrug",
        props: ['categ'],
        components: {DisplayInList},
        data() {
            return {
                dialog: false,
            }
        },
        methods: {
            toggleDialog() {
                this.dialog = !this.dialog;
            },
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
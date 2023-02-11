<template>
    <v-app-bar color="teal-darken-4">
        <v-container class="d-flex justify-center align-center">
            <v-app-bar-title class="text-h4">{{ leadTitle }}</v-app-bar-title>
            <v-spacer></v-spacer>
            
            <v-btn
                icon="mdi-cart"
                variant="elevated"
                color="teal-lighten-2"
                size="small"
                class="mr-5"
                title="Panier de médicaments"
            ></v-btn>

            <v-menu persistent>
                <template #activator="{ props }">
                    <div class="clickable" v-bind="props">
                        <v-avatar
                            image="https://randomuser.me/api/portraits/women/10.jpg"
                            size="32"
                        ></v-avatar>
                        <span class="ml-3">Nom patient</span>
                    </div>
                </template>
                <v-list>
                    <v-list-item
                        v-for="n in 5"
                        :key="n"
                    >
                        <v-list-item-title>Informations {{ n }}</v-list-item-title>
                    </v-list-item>

                    <v-divider class="my-2"></v-divider>

                    <v-list-item link @click="logout">
                        <template #prepend>
                            <v-icon>mdi-logout</v-icon>
                        </template>
                        <v-list-item-title>Se déconnecter</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>
        </v-container>
    </v-app-bar>
</template>

<script>
export default {
    data() {
        return {
        }
    },
    props: {
        leadTitle: {
            default: "PHARMA APP",
            type: String
        }
    },
    methods: {
        toggleDialog() {
            this.dialog = !this.dialog;
        },
        logout() {
            localStorage.clear();
            this.$store.dispatch('logout');
            this.$router.push('/login')
        }
    }
}
</script>

<style>
    .clickable {
        cursor: pointer;
    }
</style>
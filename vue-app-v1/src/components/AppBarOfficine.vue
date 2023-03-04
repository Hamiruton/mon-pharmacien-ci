<template>
    <v-app-bar color="teal-darken-4">
        <v-container class="d-flex justify-center align-center">
            <v-app-bar-title class="text-h4">{{ leadTitle }}</v-app-bar-title>
            <v-spacer></v-spacer>

            <v-menu persistent>
                <template #activator="{ props }">
                    <div class="clickable" v-bind="props">
                        <v-avatar
                            image="https://randomuser.me/api/portraits/women/25.jpg"
                            size="32"
                        ></v-avatar>
                        <span class="ml-3">{{ data.name }}</span>
                    </div>
                </template>
                <v-list>
                    <v-list-item prepend-icon="mdi-account-circle">
                        <v-list-item-title v-text="data.titulaire"></v-list-item-title>
                    </v-list-item>
                    <v-list-item prepend-icon="mdi-email">
                        <v-list-item-title v-text="data.email"></v-list-item-title>
                    </v-list-item>
                    <v-list-item prepend-icon="mdi-phone">
                        <v-list-item-title v-text="data.phone"></v-list-item-title>
                    </v-list-item>
                    <v-list-item prepend-icon="mdi-city">
                        <v-list-item-title v-text="data.town"></v-list-item-title>
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
    name: "AppBarOfficine",
    data() {
        return {
            data: {
                name: null,
                titulaire: null,
                phone: null,
                town: null,
                email: null
            },
        }
    },
    props: {
        leadTitle: {
            default: "PHARMA APP",
            type: String
        }
    },
    created() {
        const result = this.$store.getters.user;
        //console.log(result)
        this.data = result;
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
<template>
    <main>
        <form class="login-form" @submit.prevent="login">

            <h2 class="login-form__title">Connexion</h2>

            <v-text-field v-model="email" clearable label="Email" variant="outlined" class="w-100"></v-text-field>
            <v-text-field v-model="password" clearable label="Password" type="password" variant="outlined" class="w-100"></v-text-field>
            <v-select label="Profil" v-model="profil" clearable :items="['patient', 'officine']" variant="outlined" class="w-100"></v-select>

            <v-btn type="submit" color="teal-darken-4" class="h-100">Se connecter</v-btn>

            <v-snackbar v-model="snackbar" :color="typeAlert" :timeout="timeout">
                <v-alert :type="typeAlert" :text="textSnackbar"></v-alert>
            </v-snackbar>

            <v-row class="mt-5">
                <v-col>
                    <p class="text-down">Pas encore inscrit ? <a href="/register">Inscrivez-vous</a> | <a href="#">Mot de passe oublié</a></p>
                </v-col>
            </v-row>
        </form>
    </main>
</template>

<script>
    export default {
        name: 'LoginView',
        data() {
            return {
                snackbar: false,
                timeout: 3000,
                textSnackbar: '',
                typeAlert: '',
                email: null,
                password: null,
                profil: 'patient',
            }
        },
        beforeMount() {
            if (this.$store.getters.token) this.$router.push('/');
        },
        methods: {
            async login() {
                const credentials = {
                    email: this.email,
                    password: this.password,
                };

                const host = this.profil === 'patient' ? 'client' : 'officine';

                try {
                    const response = await this.$axios.post(`/${host}/login`, credentials);
                    const user = response.data.data;
                    console.log(user);
                    const token = user.token;
                    delete user.token;

                    if (response.data.message) {
                        this.textSnackbar = user.message;
                        this.typeAlert = "warning";
                        this.timeout = 6000;
                        this.snackbar = true;
                        return
                    }

                    await this.$store.dispatch('login', { user, token });
                    if (host === "officine") {
                        await this.$router.push('/officine/homeOfficine');
                        return
                    }
                    await this.$router.push('/');
                } catch (error) {
                    if (error.response) {
                        this.textSnackbar = error.response.data.error;
                        this.typeAlert = "error";
                        this.snackbar = true;
                        return
                    } else {
                        this.textSnackbar = error;
                        this.typeAlert = "error";
                        this.snackbar = true;
                        return
                    }
                }
            },
        },
    }
</script>

<style lang="scss" scoped>
    main {
        width: 100vw;
        height: 100vh;
        background-color: #4db6ac;
        display: grid;
        place-items: center;
    }

    .text-down {
        font-style: italic;
    }

    .text-down a {
        color: #2b2b2b;
        text-decoration: none;

        &:hover {
            color: #4db6ac;
        }
    }
    

    .login-form {
        background-color: white;
        padding: 3em 5em;
        border-radius: 7px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .login-form__title {
        text-transform: uppercase;
        font-size: 5em;
        margin-bottom: 25px;
    }

    button {
        border-radius: 60px;
        padding-block: 15px;
        width: 100%;
    }
</style>
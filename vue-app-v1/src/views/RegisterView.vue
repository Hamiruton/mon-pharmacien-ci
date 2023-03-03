<template>
    <main>
        <form class="register-form" @submit.prevent="register">

            <h2 class="register-form__title">Inscription</h2>

            
            <v-select label="Profil" v-model="profil" :items="['patient', 'officine']" variant="outlined" class="w-100"></v-select>

            <div class="w-100" v-if="profil=== 'patient'">
                <v-row>
                    <v-col cols="12">
                        <v-text-field v-model="dataPatient.fullname" label="Nom complet" variant="outlined" clearable></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="6">
                        <v-select v-model="dataPatient.sex" label="Sexe" :items="['Homme', 'Femme']" variant="outlined" clearable></v-select>
                    </v-col>
                    <v-col cols="6">
                        <v-text-field v-model="dataPatient.birthday" type="date" label="Date de naissance" variant="outlined" clearable></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="12">
                        <v-text-field v-model="dataPatient.email" label="Email" variant="outlined" clearable></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="6">
                        <v-text-field v-model="dataPatient.phone" label="Numéro" variant="outlined" clearable></v-text-field>
                    </v-col>
                    <v-col cols="6">
                        <v-text-field v-model="dataPatient.town" label="Commune" variant="outlined" clearable></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="6">
                        <v-text-field v-model="dataPatient.password" type="password" label="Mot de passe" variant="outlined" clearable></v-text-field>
                    </v-col>
                    <v-col cols="6">
                        <v-text-field v-model="confirmPwdPatient" type="password" label="Confirmer mot de passe" variant="outlined" clearable></v-text-field>
                    </v-col>
                </v-row>
            </div>


            <div class="w-100" v-if="profil=== 'officine'">
                <v-row>
                    <v-col cols="12">
                        <v-text-field v-model="dataOfficine.name" label="Nom officine" variant="outlined" clearable></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="12">
                        <v-text-field v-model="dataOfficine.titulaire" label="Nom du titulaire" variant="outlined" clearable></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="12">
                        <v-text-field v-model="dataOfficine.email" label="Email" variant="outlined" clearable></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="6">
                        <v-text-field v-model="dataOfficine.phone" label="Numéro" variant="outlined" clearable></v-text-field>
                    </v-col>
                    <v-col cols="6">
                        <v-text-field v-model="dataOfficine.town" label="Commune" variant="outlined" clearable></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="6">
                        <v-text-field v-model="dataOfficine.password" type="password" label="Mot de passe" variant="outlined" clearable></v-text-field>
                    </v-col>
                    <v-col cols="6">
                        <v-text-field v-model="confirmPwdOfficine" type="password" label="Confirmer mot de passe" variant="outlined" clearable></v-text-field>
                    </v-col>
                </v-row>
            </div>
            
            <v-btn type="submit" color="teal-darken-4" class="h-100">S'inscrire</v-btn>
            <v-snackbar v-model="snackbar" :color="typeAlert" :timeout="timeout">
                <v-alert :type="typeAlert" :text="textSnackbar"></v-alert>
            </v-snackbar>

            <v-row class="mt-5">
                <v-col>
                    <p class="text-down">Déjà inscrit ? <a href="/login">Connectez-vous</a></p>
                </v-col>
            </v-row>
            
        </form>
    </main>
</template>

<script>
    export default {
        name: 'RegisterView',
        data() {
            return {
                snackbar: false,
                timeout: 3000,
                textSnackbar: '',
                typeAlert: '',
                profil: 'patient',
                confirmPwdPatient: '',
                confirmPwdOfficine: '',
                dataPatient: {
                    fullname: '',
                    sex: '',
                    birthday: '',
                    email: '',
                    phone: '',
                    town: '',
                    password: '',
                },
                dataOfficine: {
                    name: '',
                    titulaire: '',
                    email: '',
                    phone: '',
                    town: '',
                    password: '',
                },
            }
        },
        beforeMount() {
            if (this.$store.getters.token) this.$router.push('/');
        },
        methods: {
            async register() {
                if (this.profil === 'patient' && this.dataPatient.password !== this.confirmPwdPatient) {
                    this.textSnackbar = "Les mots de passe ne concordent pas, réessayez !!!";
                    this.typeAlert = "error";
                    this.snackbar = true;
                    return
                }

                if (this.profil === 'officine' && this.dataOfficine.password !== this.confirmPwdOfficine) {
                    this.textSnackbar = "Les mots de passe ne concordent pas, réessayez !!!";
                    this.typeAlert = "error";
                    this.snackbar = true;
                    return
                }

                const credentials = this.profil === 'patient' ? this.dataPatient : this.dataOfficine;

                const host = this.profil === 'patient' ? 'client' : 'officine';

                try {
                    const response = await this.$axios.post(`/${host}/register`, credentials);
                    const user = response.data;
                    console.log(user.message === true);
                    if (user.message !== true) {
                        this.textSnackbar = user.message;
                        this.typeAlert = "warning";
                        this.timeout = 6000;
                        this.snackbar = true;
                        return
                    }
                    this.textSnackbar = "Inscription réussie";
                    this.typeAlert = "success";
                    this.timeout = 6000;
                    this.snackbar = true;
                    await this.$router.push('/login');

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

    .register-form {
        background-color: white;
        padding: 3em 5em;
        border-radius: 7px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .register-form__title {
        text-transform: uppercase;
        font-size: 5em;
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

    button {
        border-radius: 60px;
        padding-block: 15px;
        width: 100%;
        transition: background-color 300ms;
    }
</style>
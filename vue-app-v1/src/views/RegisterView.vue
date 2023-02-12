<template>
    <main>
        <form class="register-form" @submit.prevent="register">

            <h2 class="register-form__title">Inscription</h2>

            <div class="register-form__body">
                <div class="field">
                    <label for="fullname">Nom complet</label>
                    <input id="fullname" v-model="fullname" type="text" name="fullname" placeholder="Entrer votre nom complet" />
                </div>

                <v-row>
                    <v-col>
                        <div class="field">
                            <label for="sex">Sexe</label>
                            <v-select :items="['Homme', 'Femme']" variant="outlined" density="comfortable"></v-select>
                        </div>
                    </v-col>

                    <v-col>
                        <div class="field">
                            <label for="birthday">Date de naissance</label>
                            <input id="birthday" v-model="birthday" type="date" name="birthday" placeholder="" />
                        </div>
                    </v-col>
                </v-row>

                <div class="field">
                    <label for="email">Email</label>
                    <input id="email" v-model="email" type="text" name="email" placeholder="Entrer votre email" />
                </div>

                <v-row>
                    <v-col>
                        <div class="field">
                            <label for="phone">Numéro</label>
                            <input id="phone" v-model="phone" type="text" name="phone" placeholder="Entrer votre numéro" />
                        </div>
                    </v-col>

                    <v-col>
                        <div class="field">
                            <label for="commune">Commune</label>
                            <input id="commune" v-model="commune" type="text" name="commune" placeholder="Entrer votre commune" />
                        </div>
                    </v-col>
                </v-row>

                <v-row>
                    <v-col>
                        <div class="field">
                            <label for="password">Mot de passe</label>
                            <input id="password" v-model="password" type="password" name="password" placeholder="Entrer votre mot de passe" />
                        </div>
                    </v-col>

                    <v-col>
                        <div class="field">
                            <label for="confirm__password">Confirmer mot de passe</label>
                            <input id="confirm__password" v-model="confirm__password" type="password" name="confirm__password" placeholder="Entrer à nouveau le mot de passe" />
                        </div>
                    </v-col>
                </v-row>
            </div>

            <button type="submit">S'inscrire</button>
        </form>
    </main>
</template>

<script>
    export default {
        name: 'RegisterView',
        data() {
            return {
                email: null,
                password: null,
            }
        },
        beforeMount() {
            if (this.$store.getters.token) this.$router.push('/');
        },
        methods: {
            async register() {
            const credentials = {
                email: this.email,
                password: this.password,
            };

            try {
                const response = await axios.post('https://api.pros.cards/auth/login', credentials);
                const user = response.data.data;

                if (user.role !== 'ADMIN') {
                throw new Error("Vous n'êtes pas autorisé à vous connecter.");
                }

                this.$store.dispatch('login', { user, token: user.token });
                this.$router.go();
            } catch (error) {
                if (error.response) {
                alert(error.response.data.error);
                } else {
                alert(error);
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
        background-color: #f8c891;
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

    .register-form__body {
        margin-block: 1.5em;
        width: 100%;
    }

    .field {
        display: flex;
        flex-direction: column;
        gap: 5px;
        margin-block: 0.5em;
    }

    .field label {
        font-weight: 300;
    }

    .field input {
        padding: 10px 20px;
        border-radius: 60px;
        border: 1px solid #a59fbf;
        text-align: center;
    }

    button {
        $bg-color: #2b2b2b;
        background-color: $bg-color;
        color: #a59fbf;
        border-radius: 60px;
        padding-block: 15px;
        width: 100%;
        transition: background-color 300ms;

        &:hover {
            background-color: darken($bg-color, 15);
        }
    }
</style>
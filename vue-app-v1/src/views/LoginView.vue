<template>
    <main>
        <form class="login-form" @submit.prevent="login">

            <h2 class="login-form__title">Connexion</h2>

            <div class="login-form__body">
                <div class="field">
                <label for="email">Adresse email</label>
                <input id="email" v-model="email" type="email" name="email" placeholder="Adresse email" />
                </div>

                <div class="field">
                <label for="password">Mot de passe</label>
                <input id="password" v-model="password" type="password" name="password" placeholder="***" />
                </div>
            </div>

            <button type="submit">Se connecter</button>
        </form>
    </main>
</template>

<script>
    export default {
        name: 'LoginView',
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
            async login() {
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
        background-color: #4db6ac;
        display: grid;
        place-items: center;
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
    }

    .login-form__body {
        margin-block: 1.5em;
        width: 100%;
    }

    .field {
        display: flex;
        flex-direction: column;
        gap: 10px;
        margin-block: 1em;
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
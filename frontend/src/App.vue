<template>
    <div id="nav">
        <div v-if="this.$store.state.isAuthenticated">
            <button @click="$router.push('home')">Home</button>
            |
            <button v-on:click="logout">Logout</button>
        </div>
        <div v-else>
            <button @click="$router.push('sign-up')">Sign Up</button>
            |
            <button @click="$router.push('log-in')">Log In</button>
        </div>
    </div>
    <router-view/>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'App',
        beforeCreate() {
            this.$store.commit('initializeStore')

            const token = this.$store.token
            if (token) {
                axios.defaults.headers.common['Authorization'] = 'Token ' + token
            } else {
                axios.defaults.headers.common['Authorization'] = ''
            }
        },
        methods: {
            logout() {
                localStorage.clear();
                this.$router.push('/log-in')
                    .catch((err) => {console.log(err)})
                // window.location.reload();
            }
        }
    }
</script>


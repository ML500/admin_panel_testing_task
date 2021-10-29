<template>
    <div class="log-in">
        <h1>Log in</h1>
        <form @submit.prevent="submitForm">
            <input type="text" name="username" v-model="username">
            <input type="password" name="password" v-model="password">
            <button type="submit">Log In</button>
        </form>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "LogIn",
        data() {
            return {
                username: '',
                password: ''
            }
        },
        methods: {
            submitForm(e) {
                const formData = {
                    username: this.username,
                    password: this.password

                }
                axios
                    .post('api/v1/token/login', formData)
                    .then(response => {
                        const token = response.data.auth_token
                        this.$store.commit('setToken', token)
                        console.log(token)
                        axios.defaults.headers.common['Authorization'] = 'Token ' + token
                        localStorage.setItem('token', token)
                        this.$router.push('/home')
                    })
                    .catch(error => {
                        console.log(error)
                    })
            }
        }
    }
</script>

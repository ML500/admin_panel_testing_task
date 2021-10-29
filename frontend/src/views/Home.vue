<template>
    <nav class="navbar navbar-expand-sm bg-light navbar-dark">
        <ul class="navbar-nav ms-auto me-auto">
            <li class="nav-item m-1">
                <router-link class="btn btn-light btn-outline-primary"
                             to="/articles">Articles
                </router-link>
            </li>
            <li class="nav-item m-1">
                <router-link class="btn btn-light btn-outline-primary"
                             to="/categories">Categories
                </router-link>
            </li>
            <li class="nav-item m-1">
                <router-link class="btn btn-light btn-outline-primary"
                             to="/users">Users
                </router-link>
            </li>
        </ul>
    </nav>
    <router-view></router-view>
</template>

<script>
    export default {
        name: "Home"
    }
</script>

<style scoped>

</style>
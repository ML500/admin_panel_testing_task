import {createRouter, createWebHashHistory} from 'vue-router'
import SignUp from "../views/SignUp";
import LogIn from "../views/LogIn";
import Categories from "../views/Categories";
import Home from "../views/Home";
import Users from "../views/Users";
import Article from "../views/Article";

const routes = [
    {
        path: '/sign-up',
        name: 'signUp',
        component: SignUp
    },
    {
        path: '/log-in',
        name: 'logIn',
        component: LogIn
    },
    {
        path: '/home',
        name: 'home',
        component: Home,
    },
    {
        path: '/categories',
        name: 'categories',
        component: Categories

    },
    {
        path: '/users',
        name: 'users',
        component: Users

    },
    {
        path: '/articles',
        name: 'articles',
        component: Article,
    },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router

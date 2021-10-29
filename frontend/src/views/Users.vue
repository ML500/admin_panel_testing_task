<template>
    <button type="button" class="btn btn-primary m-2 fload-end"
            data-bs-toggle="modal"
            data-bs-target="#exampleModal"
            @click="addClick()">
        Add User
    </button>
    <table class="table table-striped">
        <thead>
        <tr>
            <th>
                <div class="d-flex flex-row">
                    <input class="form-control m-2"
                           v-model="UserIdFilter"
                           v-on:keyup="FilterFn()"
                           placeholder="Filter">

                    <button type="button" class="btn btn-light"
                            @click="sortResult('user_id', true)">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                             class="bi bi-arrow-down-square-fill" viewBox="0 0 16 16">
                            <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm6.5 4.5v5.793l2.146-2.147a.5.5 0 0 1 .708.708l-3 3a.5.5 0 0 1-.708 0l-3-3a.5.5 0 1 1 .708-.708L7.5 10.293V4.5a.5.5 0 0 1 1 0z"/>
                        </svg>
                    </button>
                    <button type="button" class="btn btn-light"
                            @click="sortResult('user_id', false)">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                             class="bi bi-arrow-up-square-fill" viewBox="0 0 16 16">
                            <path d="M2 16a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2zm6.5-4.5V5.707l2.146 2.147a.5.5 0 0 0 .708-.708l-3-3a.5.5 0 0 0-.708 0l-3 3a.5.5 0 1 0 .708.708L7.5 5.707V11.5a.5.5 0 0 0 1 0z"/>
                        </svg>
                    </button>
                </div>
                UserId
            </th>
            <th>
                <div class="d-flex flex-row">
                    <input class="form-control m-2"
                           v-model="UserNameFilter"
                           v-on:keyup="FilterFn()"
                           placeholder="Filter">
                    <button type="button" class="btn btn-light"
                            @click="sortResult('username', true)">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                             class="bi bi-arrow-down-square-fill" viewBox="0 0 16 16">
                            <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm6.5 4.5v5.793l2.146-2.147a.5.5 0 0 1 .708.708l-3 3a.5.5 0 0 1-.708 0l-3-3a.5.5 0 1 1 .708-.708L7.5 10.293V4.5a.5.5 0 0 1 1 0z"/>
                        </svg>
                    </button>
                    <button type="button" class="btn btn-light"
                            @click="sortResult('username', false)">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                             class="bi bi-arrow-up-square-fill" viewBox="0 0 16 16">
                            <path d="M2 16a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2zm6.5-4.5V5.707l2.146 2.147a.5.5 0 0 0 .708-.708l-3-3a.5.5 0 0 0-.708 0l-3 3a.5.5 0 1 0 .708.708L7.5 5.707V11.5a.5.5 0 0 0 1 0z"/>
                        </svg>
                    </button>

                </div>
                UserName
            </th>
            <th>
                Options
            </th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="user in users">
            <td>{{user.user_id}}</td>
            <td>{{user.username}}</td>
            <td>
                <button type="button" class="btn btn-light mr-1"
                        data-bs-toggle="modal"
                        data-bs-target="#exampleModal"
                        @click="editClick(user)">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                         class="bi bi-pencil-square" viewBox="0 0 16 16">
                        <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                        <path fill-rule="evenodd"
                              d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                    </svg>
                </button>
                <button type="button" class="btn btn-light mr-1"
                        @click="deleteClick(user.user_id)">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                         class="bi bi-trash-fill" viewBox="0 0 16 16">
                        <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1
                        1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0
                        1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                    </svg>
                </button>
            </td>
        </tr>
        </tbody>
    </table>
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">{{modalTitle}}</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="input-group mb-3">
                        <span class="input-group-text">User Name</span>
                        <input type="text" class="form-control" v-model="username">
                    </div>
                    <div class="input-group mb-3">
                        <span class="input-group-text">Password</span>
                        <input type="password" class="form-control" v-model="password">
                    </div>
                    <button type="button" @click="createClick()" v-if="user_id==0" class="btn btn-primary">Create
                    </button>
                    <button type="button" @click="updateClick()" v-if="user_id!=0" class="btn btn-primary">Update
                    </button>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "users",
        data() {
            return {
                users: [],
                modalTitle: "",
                username: "",
                password: "",
                user_id: 0,
                UserNameFilter: "",
                UserIdFilter: "",
                usersWithoutFilter: []
            }
        },
        methods: {
            refreshData() {
                axios.get("http://127.0.0.1:8000/api/v1/users/")
                    .then((response) => {
                        this.users = response.data;
                        this.usersWithoutFilter = response.data;
                    });
            },
            addClick() {
                this.modalTitle = "Add User";
                this.user_id = 0;
                this.username = '';
            },
            editClick(user) {
                this.modalTitle = "Edit User";
                this.user_id = user.user_id;
                this.username = user.username;
                this.password = user.password;

            },
            createClick() {
                axios.post("http://127.0.0.1:8000/api/v1/users/", {
                    username: this.username,
                    password: this.password
                })
                    .then((response) => {
                        this.refreshData();
                        alert(response.data);
                    });
            },
            updateClick() {
                axios.put("http://127.0.0.1:8000/api/v1/users/", {
                    user_id: this.user_id,
                    username: this.username,
                    password: this.password
                })
                    .then((response) => {
                        this.refreshData();
                        alert(response.data);
                    });
            },
            deleteClick(id) {
                if (!confirm("Are you sure?")) {
                    return;
                }
                axios.delete("http://127.0.0.1:8000/api/v1/users/" + id)
                    .then((response) => {
                        this.refreshData();
                        alert(response.data);
                    });
            },
            FilterFn() {
                var UserIdFilter = this.UserIdFilter;
                var UserNameFilter = this.UserNameFilter;

                this.users = this.usersWithoutFilter.filter(
                    function (user) {
                        return user.user_id.toString().toLowerCase().includes(
                            UserIdFilter.toString().trim().toLowerCase()
                            ) &&
                            user.username.toString().toLowerCase().includes(
                                UserNameFilter.toString().trim().toLowerCase()
                            )
                    })
            },
            sortResult(prop, asc) {
                this.users = this.usersWithoutFilter.sort(function (a, b) {
                    if (asc) {
                        return (a[prop] > b[prop]) ? 1 : ((a[prop] < b[prop]) ? -1 : 0);
                    } else {
                        return (b[prop] > a[prop]) ? 1 : ((b[prop] < a[prop]) ? -1 : 0);
                    }
                })
            }
        },
        mounted: function () {
            this.refreshData();
        }
    }
</script>

<style scoped>

</style>
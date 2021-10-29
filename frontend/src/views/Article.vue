<template>
    <div>
        <button type="button" class="btn btn-primary m-2 fload-end"
                data-bs-toggle="modal"
                data-bs-target="#exampleModal"
                @click="addClick()">
            Add Article
        </button>
        <table class="table table-striped">
            <thead>
            <tr>
                <th>
                    <div class="d-flex flex-row">
                        <input class="form-control m-2"
                               v-model="ArticleIdFilter"
                               v-on:keyup="FilterFn()"
                               placeholder="Filter">

                        <button type="button" class="btn btn-light"
                                @click="sortResult('article_id', true)">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                 class="bi bi-arrow-down-square-fill" viewBox="0 0 16 16">
                                <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm6.5 4.5v5.793l2.146-2.147a.5.5 0 0 1 .708.708l-3 3a.5.5 0 0 1-.708 0l-3-3a.5.5 0 1 1 .708-.708L7.5 10.293V4.5a.5.5 0 0 1 1 0z"/>
                            </svg>
                        </button>
                        <button type="button" class="btn btn-light"
                                @click="sortResult('article_id', false)">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                 class="bi bi-arrow-up-square-fill" viewBox="0 0 16 16">
                                <path d="M2 16a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2zm6.5-4.5V5.707l2.146 2.147a.5.5 0 0 0 .708-.708l-3-3a.5.5 0 0 0-.708 0l-3 3a.5.5 0 1 0 .708.708L7.5 5.707V11.5a.5.5 0 0 0 1 0z"/>
                            </svg>
                        </button>
                    </div>
                    ArticleId
                </th>
                <th>
                    <div class="d-flex flex-row">
                        <input class="form-control m-2"
                               v-model="ArticleNameFilter"
                               v-on:keyup="FilterFn()"
                               placeholder="Filter">
                        <button type="button" class="btn btn-light"
                                @click="sortResult('article_name', true)">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                 class="bi bi-arrow-down-square-fill" viewBox="0 0 16 16">
                                <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm6.5 4.5v5.793l2.146-2.147a.5.5 0 0 1 .708.708l-3 3a.5.5 0 0 1-.708 0l-3-3a.5.5 0 1 1 .708-.708L7.5 10.293V4.5a.5.5 0 0 1 1 0z"/>
                            </svg>
                        </button>
                        <button type="button" class="btn btn-light"
                                @click="sortResult('article_name', false)">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                 class="bi bi-arrow-up-square-fill" viewBox="0 0 16 16">
                                <path d="M2 16a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2zm6.5-4.5V5.707l2.146 2.147a.5.5 0 0 0 .708-.708l-3-3a.5.5 0 0 0-.708 0l-3 3a.5.5 0 1 0 .708.708L7.5 5.707V11.5a.5.5 0 0 0 1 0z"/>
                            </svg>
                        </button>

                    </div>
                    Article Name
                </th>
                <th>
                    Description
                </th>
                <th>
                    Category
                </th>
                <th>
                    User
                </th>
                <th>
                    Options
                </th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="article in articles">
                <td>{{article.article_id}}</td>
                <td>{{article.article_name}}</td>
                <td>{{article.article_description}}</td>
                <td v-if="article.category !== null">{{article.category.category_name}}</td>
                <td v-else></td>
                <td v-if="article.user !== null">{{article.user.username}}</td>
                <td v-else></td>
                <td>
                    <button type="button" class="btn btn-light mr-1"
                            data-bs-toggle="modal"
                            data-bs-target="#exampleModal"
                            @click="editClick(article)">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                             class="bi bi-pencil-square" viewBox="0 0 16 16">
                            <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                            <path fill-rule="evenodd"
                                  d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                        </svg>
                    </button>
                    <button type="button" class="btn btn-light mr-1"
                            @click="deleteClick(article.article_id)">
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
                        <div class="d-flex flex-row bd-highlight mb-3">
                            <div class="p-2 w-50 bd-highlight">
                                <div class="input-group mb-3">
                                    <span class="input-group-text">Article name</span>
                                    <input type="text" class="form-control" v-model="article_name">
                                </div>
                                <div class="input-group mb-3">
                                    <span class="input-group-text">Description</span>
                                    <input type="text" class="form-control" v-model="article_description">
                                </div>
                                <div class="input-group mb-3">
                                    <span class="input-group-text">Category</span>
                                    <select class="form-select" v-model="category">
                                        <option v-for="ctgr in categories" v-bind:value="ctgr.category_id">
                                            {{ctgr.category_name}}
                                        </option>
                                        <option v-bind:value=null>NONE</option>
                                    </select>
                                </div>
                                <div class="input-group mb-3">
                                    <span class="input-group-text">User</span>
                                    <select class="form-select" v-model="user">
                                        <option v-for="user in users" v-bind:value="user.user_id">
                                            {{user.username}}
                                        </option>
                                        <option v-bind:value=null>NONE</option>
                                    </select>
                                </div>
                            </div>
                            <div class="p-2 w-50 bd-highlight">
                                <img style="height:250px;width:250px;" class="images" :src="ImagePath+article_image"/>
                                <input class="m-2" type="file" @change="imageUpload">
                            </div>
                        </div>
                        <button type="button" @click="createClick()" v-if="article_id==0" class="btn btn-primary">Create
                        </button>
                        <button type="button" @click="updateClick()" v-if="article_id!=0" class="btn btn-primary">Update
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "articles",
        data() {
            return {
                articles: [],
                categories: [],
                users: [],
                modalTitle: "",
                article_name: "",
                article_description: "",
                article_id: 0,
                category: '',
                user: '',
                ArticleNameFilter: "",
                ArticleIdFilter: "",
                article_image: 'default_image.png',
                ImagePath: "http://127.0.0.1:8000/api/v1/images/",
                ArticlesWithoutFilter: [],
            }
        },
        methods: {
            refreshData() {
                axios.get("http://127.0.0.1:8000/api/v1/articles/")
                    .then((response) => {
                        this.articles = response.data;
                        this.ArticlesWithoutFilter = response.data;
                    });
                axios.get("http://127.0.0.1:8000/api/v1/categories/")
                    .then((response) => {
                        this.categories = response.data;
                    });
                axios.get("http://127.0.0.1:8000/api/v1/users/")
                    .then((response) => {
                        this.users = response.data;
                    });
            },
            addClick() {
                this.modalTitle = "Add Article";
                this.article_id = 0;
                this.article_name = '';
                this.article_description = '';
                this.category = '';
                this.user = '';
            },
            editClick(art) {
                if (art.category === null) {
                    this.category = null
                } else {
                    this.category = art.category.category_id
                }
                if (art.user === null) {
                    this.user = null
                } else {
                    this.user = art.user.user_id
                }
                this.modalTitle = "Edit Article";
                this.article_id = art.article_id;
                this.article_name = art.article_name;
                this.article_description = art.article_description;
                this.article_image = art.article_image;

            },
            createClick() {
                axios.post("http://127.0.0.1:8000/api/v1/articles/", {
                    article_name: this.article_name,
                    article_description: this.article_description,
                    category: this.category,
                    user: this.user,
                    article_image: '/' + this.article_image
                })
                    .then((response) => {
                        this.refreshData();
                        alert(response.data);
                    });
            },
            updateClick() {
                axios.put("http://127.0.0.1:8000/api/v1/articles/", {
                    article_id: this.article_id,
                    article_name: this.article_name,
                    article_description: this.article_description,
                    category: this.category,
                    user: this.user,
                    article_image: '/' + this.article_image
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
                axios.delete("http://127.0.0.1:8000/api/v1/articles/" + id)
                    .then((response) => {
                        this.refreshData();
                        alert(response.data);
                    });
            },
            FilterFn() {
                var ArticleIdFilter = this.ArticleIdFilter;
                var ArticleNameFilter = this.ArticleNameFilter;
                this.articles = this.ArticlesWithoutFilter.filter(
                    function (art) {
                        return art.article_id.toString().toLowerCase().includes(
                            ArticleIdFilter.toString().trim().toLowerCase()
                            ) &&
                            art.article_name.toString().toLowerCase().includes(
                                ArticleNameFilter.toString().trim().toLowerCase()
                            )
                    })
            },
            sortResult(prop, asc) {
                this.articles = this.ArticlesWithoutFilter.sort(function (a, b) {
                    if (asc) {
                        return (a[prop] > b[prop]) ? 1 : ((a[prop] < b[prop]) ? -1 : 0);
                    } else {
                        return (b[prop] > a[prop]) ? 1 : ((b[prop] < a[prop]) ? -1 : 0);
                    }
                })
            },
            imageUpload(event) {
                let formData = new FormData();
                formData.append('file', event.target.files[0]);
                axios.post(
                    "http://127.0.0.1:8000/api/v1/articles/save-file/",
                    formData)
                    .then((response) => {
                        this.article_image = response.data;
                    });
            },

        },
        mounted: function () {
            this.refreshData();
        }

    }
</script>
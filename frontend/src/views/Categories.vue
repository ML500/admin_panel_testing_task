<template>
    <button type="button" class="btn btn-primary m-2 fload-end"
            data-bs-toggle="modal"
            data-bs-target="#exampleModal"
            @click="addClick()">
        Add Category
    </button>
    <table class="table table-striped">
        <thead>
        <tr>
            <th>
                <div class="d-flex flex-row">
                    <input class="form-control m-2"
                           v-model="CategoryIdFilter"
                           v-on:keyup="FilterFn()"
                           placeholder="Filter">

                    <button type="button" class="btn btn-light"
                            @click="sortResult('category_id', true)">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                             class="bi bi-arrow-down-square-fill" viewBox="0 0 16 16">
                            <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm6.5 4.5v5.793l2.146-2.147a.5.5 0 0 1 .708.708l-3 3a.5.5 0 0 1-.708 0l-3-3a.5.5 0 1 1 .708-.708L7.5 10.293V4.5a.5.5 0 0 1 1 0z"/>
                        </svg>
                    </button>
                    <button type="button" class="btn btn-light"
                            @click="sortResult('category_id', false)">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                             class="bi bi-arrow-up-square-fill" viewBox="0 0 16 16">
                            <path d="M2 16a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2zm6.5-4.5V5.707l2.146 2.147a.5.5 0 0 0 .708-.708l-3-3a.5.5 0 0 0-.708 0l-3 3a.5.5 0 1 0 .708.708L7.5 5.707V11.5a.5.5 0 0 0 1 0z"/>
                        </svg>
                    </button>
                </div>
                CategoryId
            </th>
            <th>
                <div class="d-flex flex-row">
                    <input class="form-control m-2"
                           v-model="CategoryNameFilter"
                           v-on:keyup="FilterFn()"
                           placeholder="Filter">
                    <button type="button" class="btn btn-light"
                            @click="sortResult('category_name', true)">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                             class="bi bi-arrow-down-square-fill" viewBox="0 0 16 16">
                            <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm6.5 4.5v5.793l2.146-2.147a.5.5 0 0 1 .708.708l-3 3a.5.5 0 0 1-.708 0l-3-3a.5.5 0 1 1 .708-.708L7.5 10.293V4.5a.5.5 0 0 1 1 0z"/>
                        </svg>
                    </button>
                    <button type="button" class="btn btn-light"
                            @click="sortResult('category_name', false)">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                             class="bi bi-arrow-up-square-fill" viewBox="0 0 16 16">
                            <path d="M2 16a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2zm6.5-4.5V5.707l2.146 2.147a.5.5 0 0 0 .708-.708l-3-3a.5.5 0 0 0-.708 0l-3 3a.5.5 0 1 0 .708.708L7.5 5.707V11.5a.5.5 0 0 0 1 0z"/>
                        </svg>
                    </button>

                </div>
                CategoryName
            </th>
            <th>
                Parent
            </th>
            <th>
                Options
            </th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="cat in categories">
            <td>{{cat.category_id}}</td>
            <td>{{cat.category_name}}</td>
            <td v-if="cat.category_parent !== null">{{cat.category_parent.category_name}}</td>
            <td v-else></td>
            <td>
                <button type="button" class="btn btn-light mr-1"
                        data-bs-toggle="modal"
                        data-bs-target="#exampleModal"
                        @click="editClick(cat)">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                         class="bi bi-pencil-square" viewBox="0 0 16 16">
                        <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                        <path fill-rule="evenodd"
                              d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                    </svg>
                </button>
                <button type="button" class="btn btn-light mr-1"
                        @click="deleteClick(cat.category_id)">
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
                        <span class="input-group-text">Category Name</span>
                        <input type="text" class="form-control" v-model="category_name">
                    </div>
                    <div class="input-group mb-3">
                        <span class="input-group-text">Category Parent</span>
                        <select class="form-select" v-model="category_parent">
                            <option v-for="cat in categories" v-bind:value="cat.category_id">
                                {{cat.category_name}}
                            </option>
                            <option v-bind:value=null>NONE</option>
                        </select>
                    </div>
                    <button type="button" @click="createClick()" v-if="category_id==0" class="btn btn-primary">Create
                    </button>
                    <button type="button" @click="updateClick()" v-if="category_id!=0" class="btn btn-primary">Update
                    </button>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "categories",
        data() {
            return {
                categories: [],
                modalTitle: "",
                category_name: "",
                category_id: 0,
                category_parent:'',
                CategoryNameFilter: "",
                CategoryIdFilter: "",
                categoriesWithoutFilter: []
            }
        },
        methods: {
            refreshData() {
                axios.get("http://127.0.0.1:8000/api/v1/categories/")
                    .then((response) => {
                        this.categories = response.data;
                        this.categoriesWithoutFilter = response.data;
                    });
            },
            addClick() {
                this.modalTitle = "Add Category";
                this.category_id = 0;
                this.category_name = '';
            },
            editClick(cat) {
                if (cat.category_parent === null){
                    this.category_parent = null
                } else {
                    this.category_parent = cat.category_parent.category_id
                }
                this.modalTitle = "Edit Category";
                this.category_id = cat.category_id;
                this.category_name = cat.category_name;
            },
            createClick() {
                axios.post("http://127.0.0.1:8000/api/v1/categories/", {
                    category_name: this.category_name,
                    category_parent: this.category_parent
                })
                    .then((response) => {
                        this.refreshData();
                        alert(response.data);
                    });
            },
            updateClick() {
                axios.put("http://127.0.0.1:8000/api/v1/categories/", {
                    category_id: this.category_id,
                    category_name: this.category_name,
                    category_parent: this.category_parent
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
                axios.delete("http://127.0.0.1:8000/api/v1/categories/" + id)
                    .then((response) => {
                        this.refreshData();
                        alert(response.data);
                    });
            },
            FilterFn() {
                var CategoryIdFilter = this.CategoryIdFilter;
                var CategoryNameFilter = this.CategoryNameFilter;
                console.log(this.categoriesWithoutFilter)
                this.categories = this.categoriesWithoutFilter.filter(
                    function (ct) {
                        return ct.category_id.toString().toLowerCase().includes(
                            CategoryIdFilter.toString().trim().toLowerCase()
                            ) &&
                            ct.category_name.toString().toLowerCase().includes(
                                CategoryNameFilter.toString().trim().toLowerCase()
                            )
                    })
            },
            sortResult(prop, asc) {
                this.categories = this.categoriesWithoutFilter.sort(function (a, b) {
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
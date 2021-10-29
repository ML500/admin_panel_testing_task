import { createStore } from 'vuex'

export default createStore({
  state: {
    token: '',
    isAuthenticated: false
  },
  mutations: {
    initializeStore(state){
      //
      // console.log(state, 'staaate')
      // console.log(localStorage, 'localStorageeee')
      if (localStorage.getItem('token')){
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
      } else {
        state.token = ''
        state.isAuthenticated = false
      }
    },
    setToken(state, token){
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state){
      state.token = ''
      state.isAuthenticated = false
    }
  },
  actions: {
  },
  modules: {
  }
})

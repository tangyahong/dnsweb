const state = {
    isAuthenticated: false,
        currentUser: '王小虎',
        token:''
}

const mutations = {
    changeAuthenticationState(state) {
        state.isAuthenticated = true
    },

    changeToken(state, token) {
        localStorage.getItem('token')
        state.token = token
    }
}

export default {
    state,
    mutations
}
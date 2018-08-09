import Vue from 'vue'
import Vuex from 'vuex'
import authModule from './authModule'

Vue.use(Vuex);

export default new Vuex.Store({
    modules:{
        authModule
    }
})


/* import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
    isCollapse: false
}

const mutations = {
    CHANGE(state) {
        state.isCollapse = !state.isCollapse
    }
}

const actions = {
    change({ commit }) {
        commit("CHANGE")
    }
}

export default new Vuex.Store({
    state,
    mutations,
    actions
}) */
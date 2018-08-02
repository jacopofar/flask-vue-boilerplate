import Vue from 'vue';
import axios from 'axios';

const state = {
  loggedIn: false,
  myName: null,
  myMail: null,
};

const getters = {
  loggedIn: state => state.loggedIn,
  name: state => state.myName,
  mail: state => state.myMail,
};

const mutations = {
  setLoggedIn(state, { loggedIn, mail, name }) {
    Vue.set(state, 'loggedIn', loggedIn);
    if (loggedIn) {
      Vue.set(state, 'myMail', mail);
      Vue.set(state, 'myName', name);
    }
  },
};

const actions = {
  /** Check whether the user is logged in, and if so populates the state. */
  ensureLogIn({ commit }) {
    axios.get('/login/whoami').then((response) => {
      commit('setLoggedIn', { loggedIn: true, mail: response.data.mail, name: response.data.name });
    }).catch((error) => {
      console.error(error);
      commit('setLoggedIn', { loggedIn: false });
    });
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};

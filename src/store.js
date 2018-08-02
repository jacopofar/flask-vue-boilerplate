import Vue from 'vue';
import Vuex from 'vuex';
import session from '@/store/session';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    session,
  },
});

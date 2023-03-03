import { createStore } from 'vuex';

export default createStore ({
	state: {
		token: localStorage.getItem('token'),
	},
	getters: {
		user: () => (localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')) : null),
		token: () => localStorage.getItem('token'),
	},
	mutations: {},
	actions: {
		login(store, { user, token }) {
			localStorage.setItem('user', JSON.stringify(user));
			localStorage.setItem('token', token);
			window.location.reload()
		},
		logout() {
			localStorage.clear();
			window.location.reload();
		},
	},
});

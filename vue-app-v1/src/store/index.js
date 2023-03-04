import { createStore } from 'vuex';

export default createStore ({
	state: {
		token: localStorage.getItem('token'),
	},
	getters: {
		user: () => (localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')) : null),
		idUser: () => (JSON.parse(localStorage.getItem('user'))._id),
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
		async getAllMolecules(_, { axios }) {
			let molecules = (await axios.get('/officine/molecules/get-all')).data.data;

			let listeMol = [];
			molecules.filter(obj => {
				listeMol.push(obj.nameMol/*.toUpperCase()*/);
			});
			return listeMol;
		},
		async getAllDrugCat(_, { axios }) {
			let drugsCat = (await axios.get('/officine/categDrugs/get-all')).data.data;
			
			/*
			let listeDrug = [];
			drugsCat.filter(ind => {
				listeDrug.push(ind.toUpperCase())
			});
			*/
			return drugsCat;
		},
		async getMoleculeById(_, { axios, idMol }) {
			let nameMol = (await axios.get(`/officine/molecule/${idMol}`)).data.data;
			
			return nameMol;
		},
		async getAffiliatedOfficineByNameMedoc(_, { axios, nameMedoc }) {
			let listeAff = (await axios.get(`/client/medocs/name/${nameMedoc}`)).data.data;
			
			return listeAff;
		}
	},
});

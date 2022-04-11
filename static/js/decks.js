const key = localStorage.getItem('key');
console.log(key.substring(1, 84))
const k = key.substring(1, 84)

const store = new Vuex.Store({
    state: {
        deck: 'Sachin',
        ids: -1,
    },
    getters: {
        getDeck: function (state) {
            return state.deck
        }
    },
    mutations: {
        setDeck: function (state, name) {
            state.deck = name
        },
        setID: function (state, id) {
            state.ids = id
        }
    }

})

const app = new Vue({
    el: '#app',
    data: function () {
        return {
            decks: [],
        }
    },
    components: {
        // To be added
    },
    async created() {
        // use created for api calls
        const a = await fetch('/api/deck?auth_token=' + k, {
            method: 'GET', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, *cors, same-origin
        })
        const b = await a.json()
        console.log(b)
        b.forEach(element => {
            this.decks.push(element)
        });
    },
    store: store,
    methods: {
        setd: function (deck, id) {
            console.log(deck)
            console.log(id);
            this.$store.commit('setDeck', deck)
            this.$store.commit('setID', id)

        },
        updateValue: function () {
            const t = document.getElementById('UpdateDeck').value
            const i = document.getElementById('UpdateId').value
            console.log(i);
            const pay = {
                "name": t
            }
            const a = fetch('/api/deck/' + i + '?auth_token=' + k, {
                method: 'PUT', // *GET, POST, PUT, DELETE, etc.
                mode: 'cors', // no-cors, *cors, same-origin
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(pay) // body data type must match
            })
            location.reload('/')
        },
        deleteValue: function (deck, id) {
            this.$store.commit('setDeck', deck)
            this.$store.commit('setID', id)
            const i = this.$store.state.ids
            console.log(i);
            const a = fetch('/api/deck/' + i + '?auth_token=' + k, {
                method: 'DELETE',
                mode: 'cors',
            })
            location.reload('/')
        }
    },
    computed: {
        temp() {
            return this.$store.state.deck
        },
        tid() {
            return this.$store.state.ids
        }
    },
    watch: {

    }
})
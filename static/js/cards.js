const key = localStorage.getItem('key');
console.log(key.substring(1, 84))
const k = key.substring(1, 84)

const app = new Vue({
    el: "#app",
    data: function () {
        return {
            deck_id: document.getElementById('main').innerText,
            // cards array by deck
            cards: [],
            // for create
            top: 'Enter front',
            bottom: 'Enter back',
            // for update model
            head: '',
            tail: '',
            coin: '', // card id
        }
    },
    methods: {
        getCards: async function () {
            const a = await fetch('/api/cardsbydeck/' + this.deck_id + '?auth_token=' + k, {
                method: 'GET', // *GET, POST, PUT, DELETE, etc.
                mode: 'cors', // no-cors, *cors, same-origin
            })
            const b = await a.json()
            temp = []
            b.forEach(element => {
                temp.push(element)
            });
            this.cards = temp
            console.log(temp);
        },
        create: async function () {
            const pay = {
                "front": this.top,
                "back": this.bottom,
                "deck_id": this.deck_id
            }
            fetch('/api/card' + '?auth_token=' + k, {
                method: 'POST', // *GET, POST, PUT, DELETE, etc.
                mode: 'cors', // no-cors, *cors, same-origin
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(pay) // body data type must match "Content-Type" header
            })
                .then(response => response.json())
                .then(data => console.log(data))

            location.reload('/')
        },
        deleteValue: function (id) {
            console.log(id);
            const a = fetch('/api/card/' + id + '?auth_token=' + k, {
                method: 'DELETE',
                mode: 'cors',
            })
            location.reload('/')
        },
        update: function (id, front, back) {
            console.log(id);
            console.log(front);
            console.log(back);
            this.head = front
            this.tail = back
            this.coin = id // card id
        },
        save: function () {
            const pay = {
                "front": this.head,
                "back": this.tail,
                "deck_id": this.deck_id
            }
            console.log();
            fetch('/api/card/' + this.coin + '?auth_token=' + k, {
                method: 'PUT', // *GET, POST, PUT, DELETE, etc.
                mode: 'cors', // no-cors, *cors, same-origin
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(pay) // body data type must match "Content-Type" header
            })
                .then(response => response.json())
                .then(data => console.log(data))

            location.reload('/')
        }
    },
    computed: {

    }
})
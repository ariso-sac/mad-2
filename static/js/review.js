const key = localStorage.getItem('key');
console.log(key.substring(1, 84))
const k = key.substring(1, 84)

const app = new Vue({
    el: '#app',
    data: function () {
        return {
            deck_id: document.getElementById("main").innerHTML,
            uid: document.getElementById("user").innerHTML,
            cards: [],
            i: 0,
            end: -1,
            doubt: 'Hi',
            solution: 'Hello',
            easy: 0,
            medium: 0,
            hard: 0,
        }
    },
    async created() {
        // use created for api calls
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
        this.end = temp.length
        console.log(temp);
        this.doubt = this.cards[0].front
        this.solution = this.cards[0].back
    },
    methods: {
        eUpdate: function () {
            this.easy += 1
        },
        mUpdate: function () {
            this.medium += 1
        },
        hUpdate: function () {
            this.hard += 1
        },
        showAns: function () {
            const a = document.getElementById('Answer')
            a.style.display = "block"
            const x = document.getElementById('Feedback')
            x.style.display = "block"
            const b = document.getElementById('Question')
            b.style.display = "none"
            //Ques Counter
            this.i += 1
        },
        showQues: function () {
            const a = document.getElementById('Answer')
            a.style.display = "none"
            const x = document.getElementById('Feedback')
            x.style.display = "none"
            const b = document.getElementById('Question')
            b.style.display = "block"
            //
            if (this.i == this.end) {
                b.style.display = "none"
                const Z = document.getElementById('End')
                Z.style.display = "block"
            } else {
                this.doubt = this.cards[this.i].front
                this.solution = this.cards[this.i].back
            }
        },
        save: async function () {
            const P = await fetch('/api/user/' + 1 + '/deck/' + this.deck_id + '?auth_token=' + k, {
                method: 'DELETE',
                mode: 'cors',
            })
            const pay = {
                "easy": this.easy,
                "moderate": this.medium,
                "hard": this.hard
            }
            const a = await fetch('/api/user/' + 1 + '/deck/' + this.deck_id + '?auth_token=' + k, {
                method: 'POST',
                mode: 'cors',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(pay)
            })
            const b = a.json()
            console.log(b.status);
        }
    },
    computed: {

    }
})
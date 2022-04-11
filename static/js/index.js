const key = localStorage.getItem('key');
console.log(key.substring(1,84))
const k=key.substring(1,84)

const card = {
    // use props for JSX attributes
    props: ['ids','deck','updated_on','uid'],
    template: `<div class='col'>
    <div class="card text-white bg-dark mb-3" style="max-width: 18rem;">
        <div class="card-body">
            <h5 class="card-title">{{deck}}</h5>
            <p class="card-text">
                <small>
                    Scores: 
                    Easy : {{easy}} 
                    Moderate: {{moderate}}
                    Hard : {{hard}}
                </small>
                <small>Last ReView on: {{review_on}}</small>
                <small>Last Updated on: {{updated_on}}</small>
            </p>
            <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                    <a type="button" :href="'/review/'+ids+'/'+deck"
                        class="btn btn-sm btn-outline-secondary">ReView</a>
                    <a type="button" :href="'/cards/'+ids+'/'+deck"
                        class="btn btn-sm btn-outline-secondary">Manage</a>
                </div>
            </div>
        </div>
    </div>
</div>
`,
    data: function () {
        return{
            easy: 0,
            moderate: 0,
            hard: 0,
            review_on:0
        }
    },
    async created() {
        // use created for api calls
        const a = await fetch('/api/user/'+this.uid+'/deck/'+this.ids+'?auth_token='+k, {
            method: 'GET', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, *cors, same-origin
        })
        const b = await a.json()
        console.log(b)
        this.easy=b.easy
        this.moderate=b.moderate
        this.hard=b.hard
        this.review_on=b.updated_on
    },
}

const app = new Vue({
    el: '#app',
    data: function () {
        return {
            decks: [],
        }
    },
    components: {
        card
    },
    async created() {
        // use created for api calls
        const a = await fetch('/api/deck?auth_token='+k, {
            method: 'GET', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, *cors, same-origin
        })
        const b = await a.json()
        console.log(b)
        b.forEach(element => {
            this.decks.push(element)
        });
    },
    methods: {
    }
})
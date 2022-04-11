const app = new Vue({
    el: '#app',
    data: function () {
        return {
            user:'',
            pass:'',
        }
    },
    async created() {
        await fetch('/logout')
        .then(response=>console.log(response.status))
        localStorage.clear()
    },
    methods: {
        setkey() {
            // var user = document.getElementById('user').value
            // var pass = document.getElementById('pass').value
            var pay = { "email": this.user, "password": this.pass }
            console.log(user, pass)
            fetch('/login?include_auth_token', {
                method: 'POST', // *GET, POST, PUT, DELETE, etc.
                mode: 'cors', // no-cors, *cors, same-origin
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(pay) // body data type must match "Content-Type" header
            })
                .then(response => response.json())
                .then(data => this.putkey(data))
        },
        putkey(key) {
            var v=key.response.user.authentication_token
            localStorage.setItem('key', JSON.stringify(v));
            console.log(v)
            this.changeUrl()
        },
        changeUrl() {
            window.location.replace("/dashboard")
        }
    }
})
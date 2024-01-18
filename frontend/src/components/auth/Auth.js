

const Otp = (email) => {
    fetch('/api/auth/otp', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: email })
    })
        .then(res => res.json())
        .then(res => {
            if (res.success) {
                console.log(res.msg);
                // enregistre le token dans le local storage
                
            } else {
                console.log(res.msg);
            }
        })
        .catch(err => console.log(err));
}

export { Otp};

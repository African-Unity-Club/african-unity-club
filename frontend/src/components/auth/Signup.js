import React from 'react';
import '../style/Sign.css'



class SignUp extends React.Component {
        
    constructor(props) {
        super(props);
        this.state = {
            username: '',
            email: '',
            password: '',
        }
    }

    // mets a jour le state a chaque changement dans le formulaire
    handleChange = (e) => {
        this.setState({ [e.target.name]: e.target.value });
    }

    // envoie les donnees du formulaire au serveur
    handleSubmmit = (e) => {
        e.preventDefault();

        if (this.state.username.length < 3) {
            document.getElementById('username').nextSibling.innerHTML = 'Username must be at least 3 characters';
        } else {
            document.getElementById('username').nextSibling.innerHTML = '';
        }

        if (!this.state.email.includes('@')) {
            document.getElementById('email').nextSibling.innerHTML = 'Invalid email';
        } else {
            document.getElementById('email').nextSibling.innerHTML = '';
        }

        if (this.state.password.length < 8) {
            document.getElementById('password').nextSibling.innerHTML = 'Password must be at least 8 characters';
        } else {
            document.getElementById('password').nextSibling.innerHTML = '';
        }

        const password2 = document.getElementById('password2').value;
        if (this.state.password !== password2) {
            password2.nextSibling.innerHTML = 'Passwords do not match';
        } else {
            password2.nextSibling.innerHTML = '';
            this.optUser();
        }
    }

    // envoie un lien de verification par email pour l'inscription
    handleOtp = () => {
        fetch('/api/auth/otp', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email: this.state.email })
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

    render() {

        return (
            <main className='vwh'>
                <div className='picture-1'>
                    <div className='logo'></div>
                </div>
                <div className='signup'>
                    <h1 className='order-1 title'>Sign Up</h1>
                    <form className='form' onSubmit={this.handleSubmmit}>
                        <div className='form-group'>
                            <label for='username'>Username</label>
                            <input 
                                type='text'
                                id='username'
                                name='username'
                                value={this.state.username}
                                onChange={this.handleChange}
                                required
                            />
                            <span className='error-message'></span>
                        </div>
                        <div className='form-group'>
                            <label for='email'>Email</label>
                            <input 
                                type='email'
                                id='email'
                                name='email'
                                value={this.state.email}
                                onChange={this.handleChange}
                                required
                            />
                            <span className='error-message'></span>
                        </div>
                        <div className='form-group'>
                            <label for='password'>Password</label>
                            <input 
                                type='password'
                                id='password'
                                name='password'
                                value={this.state.password}
                                onChange={this.handleChange}
                                required
                            />
                            <span className='error-message'></span>
                        </div>
                        <button type='submit' className='btn btn-primary'>Sign Up</button>
                    </form>
                </div>
            </main>
        );
    }
}

export default SignUp

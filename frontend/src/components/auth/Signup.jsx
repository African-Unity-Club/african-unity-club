import { useState } from 'react';
import { Otp } from './Auth';
import '../style/Sign.css'



function SignUp() {
    
    const [params, setParams] = useState({
        username: '',
        email: '',
        password: '',
    });

    const handleChange = (e) => {
        setParams({ ...params, [e.target.name]: e.target.value });
    }

    const handleSubmmit = (e) => {
        e.preventDefault();

        if (params.username.length < 3) {
            document.getElementById('username').nextSibling.innerHTML = 'Username must be at least 3 characters';
        } else {
            document.getElementById('username').nextSibling.innerHTML = '';
        }

        if (!params.email.includes('@')) {
            document.getElementById('email').nextSibling.innerHTML = 'Invalid email';
        } else {
            document.getElementById('email').nextSibling.innerHTML = '';
        }

        if (params.password.length < 8) {
            document.getElementById('password').nextSibling.innerHTML = 'Password must be at least 8 characters';
        } else {
            document.getElementById('password').nextSibling.innerHTML = '';
        }

        const password2 = document.getElementById('password2').value;
        if (params.password !== password2) {
            password2.nextSibling.innerHTML = 'Passwords do not match';
        } else {
            password2.nextSibling.innerHTML = '';
            Otp();
        }
    }


    return (
        <main className='vwh'>
            <div className='picture-1'>
                <div className='logo'></div>
            </div>
            <div className='signup'>
                <h1 className='order-1 title'>Sign Up</h1>
                <form className='form' onSubmit={handleSubmmit}>
                    <div className='form-group'>
                        <label for='username'>Username</label>
                        <input 
                            type='text'
                            id='username'
                            name='username'
                            value={params.username}
                            onChange={handleChange}
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
                            value={params.email}
                            onChange={handleChange}
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
                            value={params.password}
                            onChange={handleChange}
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


export default SignUp

import { useState } from 'react';
import { Otp } from './Auth';
import '../../style/Sign.css'

import { Link } from 'react-router-dom'



function SignUp() {
    
    const [params, setParams] = useState({
        username: '',
        email: '',
        password: '',
        password2: '',
    });

    const [errors, setErrors] = useState({
        username: '',
        email: '',
        password: '',
        password2: '',
    });

    const handleChange = (e) => {
        setParams({ ...params, [e.target.name]: e.target.value });
        setErrors({ ...errors, [e.target.name]: '' });
    }

    const handleSubmmit = (e) => {
        e.preventDefault();

        const newErrors = {
            username: params.username.length < 4 ? 'Username must be at least 3 characters' : '',
            email: !params.email.includes('@') ? 'Invalid email' : '',
            password: params.password.length < 8 ? 'Password must be at least 8 characters' : '',
            password2: params.password2 !== params.password ? 'Password must be at least 8 characters' : '',
        };

        setErrors(newErrors);

        if (Object.values(newErrors).every(error => error === '')) {

            setErrors((prevErrors) => ({ ...prevErrors, password: '' }));
            const token = Otp(params.email);
                // token = {'otp': otp, 'expired': expired, 'email': email}
                // sauvegarder les données dans la base de données redis local
                // redis.set(params.email, token.otp, token.expired)
        }
    };


    return (
        <main className='vwh sign'>
            <div className='picture-1'>
                <div className='logo'></div>
            </div>
            <div className='signup'>
                <h1 className='order-1 title'>Sign Up</h1>
                <form className='form' onSubmit={handleSubmmit} method='post'>
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
                        <span className='error-message'>{errors.username}</span>
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
                        <span className='error-message'>{errors.email}</span>
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
                        <span className='error-message'>{errors.password}</span>
                    </div>
                    <div className='form-group'>
                        <label for='password'>Confirm Password</label>
                        <input 
                            type='password'
                            id='password2'
                            name='password2'
                            value={params.password2}
                            onChange={handleChange}
                            required
                        />
                        <span className='error-message'>{errors.password2}</span>
                    </div>
                    <button type='submit' className='btn btn-primary'>Register</button>
                </form>
                <div className='other'>
                    <span className='foot-other'>already have an account</span>
                    <Link to="/signin" className='foot-other'>click to connect</Link>
                </div>
            </div>
        </main>
    );
}


export default SignUp

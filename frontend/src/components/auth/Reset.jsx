import React, { useState } from 'react'
import '../../style/Sign.css'

function ResetPassword() {

    const [params, setParams] = useState(
        {
            password: '',
            confirm: ''
        }
    )

    const [error, setError] = useState(
        {
            password: '',
            confirm: ''
        }
    )

    const handleChange = (e) => {
        setParams({...params, [e.target.name]: e.target.value})
        setError({...error, [e.target.name]: ''})
    }

    const handleSubmit = (e) => {
        e.preventDefault()

        const newError = {
            password: params.password.length < 8 ? 'Password must be at least 8 characters' : '',
            confirm: params.confirm !== params.password ? 'confirm password not equal to password' : '',
        }

        setError(newError)

        if (Object.values(newError).every(error => error === '')) {
            // fetch
        }
    }


    return (
        <main className='vwh sign'>
            <div className='picture-3'>
                <div className='logo'></div>
            </div>
            <div className='signup'>
                <h1 className='order-1 title'>Reset Password</h1>
                <form className='form' method='post' onSubmit={handleSubmit}>
                    <div className='form-group'>
                        <label for='password'>New Password</label>
                        <input
                            type='password'
                            id='password'
                            name='password'
                            value={params.password}
                            onChange={handleChange}
                            required
                        />
                        <span className='error'>{error.password}</span>
                    </div>
                    <div className='form-group'>
                        <label for='password'>Confirm Password</label>
                        <input
                            type='password'
                            id='confirm'
                            name='confirm'
                            value={params.confirm}
                            onChange={handleChange}
                            required
                        />
                        <span className='error'>{error.confirm}</span>
                    </div>
                    <div className='form-group'>
                        <button className='btn btn-primary' type='submit'>Reset</button>
                    </div>
                </form>
            </div>
        </main>
    )
}

export default ResetPassword

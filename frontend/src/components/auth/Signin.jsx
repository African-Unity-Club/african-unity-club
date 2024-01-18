import '../../style/Sign.css'
import { useState } from 'react'
import { Link } from "react-router-dom";


function SignIn() {

    const [auth, setAuth] = useState(
        {
            email: '',
            password: ''
        }
    )

    const handleChange = (e) => {
        setAuth({...auth, [e.target.name]: e.target.value})
    }

    const handleSubmit = (e) => {

        const url = ''
        fetch(url,
            {
                method: 'POST',
                header: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(
                    {
                        email: auth.email,
                        password: auth.password
                    }
                )
            }
        )
            .then(res => res.json())
            .then(res => {
                if (res.success)  {
                    // sauvegarde des infos dans redis
                    // redirection vers Dash
                } else {
                    console.log(res.msg)
                    return null
                }
            })
    }

    return (
        <main className='vwh'>
            <div className='picture-1'>
                <div className='logo'></div>
            </div>
            <div className='signin'>
                <h1 className='order-1 title'>Sign In</h1>
                <form className='form' onSubmit={handleSubmit}>
                    <div className='form-group'>
                        <label for='email'>Email</label>
                        <input
                            type='email'
                            id='email'
                            name='email'
                            value={auth.email}
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
                            value={auth.password}
                            onChange={handleChange}
                            required
                        />
                        <span className='error-message'></span>
                    </div>
                    <div className='action'>
                        <Link to="/signup">Sign Up</Link>
                        <button type='submit' className='btn btn-primary'>Connexion</button>
                    </div>
                </form>
            </div>
        </main>
    )

}

export default SignIn

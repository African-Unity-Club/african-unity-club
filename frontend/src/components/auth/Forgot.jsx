import '../../style/Sign.css'
import { useState} from 'react';



function Forgot() {

    const [email, setEmail] = useState('')

    const handleChange = (e) => {
        setEmail(e.target.value)
    }

    const handleSubmmit = (e) => {
        // send email with url to reset password by token
    } 

    return (
        <main className='vwh sign verify'>
            <div className='verifyotp'>
                <h1 className='order-1 title'>Reset password</h1>
                <form className='form' method='post' onSubmit={handleSubmmit}>
                    <div className='info'>
                        Enter your email address and we'll send you a link to reset your password
                    </div>
                    <div className='form-group'>
                        <input 
                            type="text"
                            id='email'
                            name='email'
                            onChange={handleChange}
                            required 
                        />
                        <span className='error'></span>
                    </div>
                </form>
            </div>
        </main>
    )
}

export default Forgot

import '../../style/Sign.css'
import { useState } from 'react';
import { Otp } from './Auth';



function VerifyOtp() {

    const [otp, setOtp] = useState('');

    const handleSubmmit = (e) => {
        e.preventDefault();

        if (otp.length < 6) {
            document.getElementById('otp').nextSibling.innerHTML = 'OTP must be at least 6 characters';
        } else {
            document.getElementById('otp').nextSibling.innerHTML = '';
            // const token = redis.get(params.email)
            // if (token.otp === otp) {
            //     if (token.expired > Date.now()) {
            //         // sauvegarder les données dans la base de données mongo
            //         // mongo.save(params.username, params.email, params.password)
            //     } else {
            //         document.getElementById('otp').nextSibling.innerHTML = 'OTP expired';
            //     }
            // } else {
            //     document.getElementById('otp').nextSibling.innerHTML = 'OTP invalid';
            // }
        }
    }

    return (
        <main className='vwh'>
            <div className='picture-1'>
                <div className='logo'></div>
            </div>
            <div className='verifyotp'>
                <h1 className='order-1 title'>Sign Up</h1>
                <form className='form' onSubmit={handleSubmmit}>
                    <div className='info'>
                        Verifier vos email
                    </div>
                    <div className=''>
                        <input 
                            type="text"
                            id='otp'
                            name='otp'
                            value={otp}
                            onChange={(e) => setOtp(e.target.value)}
                            required 
                        />
                        <span className='error'></span>
                    </div>
                    <div className='res'>
                        <a href='/signup' className='btn btn-primary'>Resend OTP</a>
                        <button type='submit' className='btn btn-primary'>Verify OTP</button>
                    </div>
                </form>
            </div>
        </main>
    )
}

export default VerifyOtp
